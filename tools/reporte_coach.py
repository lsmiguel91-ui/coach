# -*- coding: utf-8 -*-
"""Generador del reporte semanal en PDF — Coach de Luis Miguel.
Uso: python3 reporte_coach.py analisis.json salida.pdf
El JSON de análisis lo escribe Claude cada domingo (datos + textos).
PDF liviano: fuentes estándar (Helvetica) y gráficos vectoriales; si hay qpdf, se recomprime al final.
"""
import json, sys, io, os, glob, subprocess
try:
    import svglib  # gráficos vectoriales: PDF liviano (~15 KB) que se puede subir a Drive automáticamente
except ImportError:
    subprocess.run([sys.executable,'-m','pip','install','-q','--break-system-packages','svglib'],check=True)
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table,
                                TableStyle, Image, KeepTogether, PageBreak)
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# ---------- paleta (igual que la app, opción B) ----------
PRI='#5F829B'; PRI2='#8DA9BD'; SOFT='#E2EBF2'; HL='#EEF3F7'; TXT='#2B3742'; MUT='#7B8894'
OK='#4E9A73'; WARN='#E0A93B'; BAD='#C8574B'; BORDER='#D9E2EA'
SEM={'verde':(OK,'','VAS MEJORANDO'),'amarillo':(WARN,'','ATENCIÓN'),'rojo':(BAD,'','HAY QUE AJUSTAR')}

plt.rcParams['svg.fonttype']='none'; plt.rcParams['font.family']='sans-serif'; plt.rcParams['font.sans-serif']=['Helvetica','Arial','DejaVu Sans']
plt.rcParams.update({'font.size':9,'axes.edgecolor':BORDER,'axes.labelcolor':MUT,'xtick.color':MUT,'ytick.color':MUT,
                     'axes.spines.top':False,'axes.spines.right':False,'axes.grid':True,'grid.color':HL,'grid.linewidth':0.8})

S=lambda **k: ParagraphStyle('x',fontName=k.pop('f','Helvetica'),fontSize=k.pop('s',9.5),leading=k.pop('l',13.5),textColor=k.pop('c',TXT),**k)
H1=S(f='Helvetica-Bold',s=17,l=21,c=PRI); H2=S(f='Helvetica-Bold',s=12.5,l=16,c=TXT,spaceBefore=6,spaceAfter=4)
P=S(); PM=S(c=MUT,s=8.5,l=11.5); SMALL=S(s=8,l=10.5,c=MUT)

def fig_img(fig,w=170):
    from svglib.svglib import svg2rlg
    b=io.BytesIO(); fig.savefig(b,format='svg',bbox_inches='tight'); plt.close(fig); b.seek(0)
    dr=svg2rlg(b); k=w*mm/dr.width; dr.width*=k; dr.height*=k; dr.scale(k,k); return dr

def num(x):
    try: return float(str(x).replace(',','.'))
    except: return None

def box(content,bg=HL,border=BORDER,pad=8):
    t=Table([[content]],colWidths=[170*mm]); t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),colors.HexColor(bg)),
      ('BOX',(0,0),(-1,-1),0.6,colors.HexColor(border)),('LEFTPADDING',(0,0),(-1,-1),pad),('RIGHTPADDING',(0,0),(-1,-1),pad),
      ('TOPPADDING',(0,0),(-1,-1),pad),('BOTTOMPADDING',(0,0),(-1,-1),pad)])); return t

def kpis(items):
    cells=[[Paragraph(f'<font name="Helvetica-Bold" size="16" color="{PRI}">{v}</font><br/><font size="7.5" color="{MUT}">{l}</font>',S(alignment=1,l=17)) for v,l in items]]
    t=Table(cells,colWidths=[170*mm/len(items)]*len(items))
    t.setStyle(TableStyle([('BOX',(0,0),(-1,-1),0.6,colors.HexColor(BORDER)),('INNERGRID',(0,0),(-1,-1),0.6,colors.HexColor(BORDER)),
      ('BACKGROUND',(0,0),(-1,-1),colors.white),('TOPPADDING',(0,0),(-1,-1),8),('BOTTOMPADDING',(0,0),(-1,-1),8)])); return t

def header_footer(c,doc):
    c.saveState(); W,H=A4
    c.setFillColor(colors.HexColor(PRI)); c.rect(0,H-14*mm,W,14*mm,fill=1,stroke=0)
    c.setFillColor(colors.white); c.setFont('Helvetica-Bold',11); c.drawString(20*mm,H-9*mm,'Coach de Luis Miguel · Reporte semanal')
    c.setFont('Helvetica',9); c.drawRightString(W-20*mm,H-9*mm,doc._sub)
    c.setFillColor(colors.HexColor(MUT)); c.setFont('Helvetica',7.5); c.drawRightString(W-20*mm,10*mm,f'Página {doc.page}')
    c.restoreState()

DIAS=['Lun','Mar','Mié','Jue','Vie','Sáb','Dom']
RUN={'trote','intervalos','ritmo','fondo'}

def build(A,out):
    dias=A['dias']; sem=SEM.get(A.get('semaforo','amarillo'),SEM['amarillo'])
    doc=BaseDocTemplate(out,pagesize=A4,leftMargin=20*mm,rightMargin=20*mm,topMargin=22*mm,bottomMargin=16*mm,
                        title=f"Reporte semana {A['semana']}",author='Coach de Luis Miguel')
    doc._sub=f"Semana {A['semana']} · {A['rango']}"
    doc.addPageTemplates([PageTemplate(frames=[Frame(20*mm,16*mm,170*mm,A4[1]-38*mm,id='f')],onPage=header_footer)])
    E=[]
    # ---- portada / resumen ----
    E.append(Paragraph(f"Semana {A['semana']}",H1)); E.append(Paragraph(A['rango'],PM)); E.append(Spacer(1,8))
    sem_t=Table([[Paragraph(f'<font name="Helvetica-Bold" size="13" color="white">{sem[2]}</font><br/><font color="white" size="9.5">{A["titular"]}</font>',S(l=15))]],colWidths=[170*mm])
    sem_t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),colors.HexColor(sem[0])),('LEFTPADDING',(0,0),(-1,-1),12),('TOPPADDING',(0,0),(-1,-1),10),('BOTTOMPADDING',(0,0),(-1,-1),10)]))
    E+= [sem_t,Spacer(1,10)]
    plan=[d for d in dias if d.get('tipo')!='descanso']; hechos=[d for d in plan if d.get('hecho')]
    runs=[d for d in dias if d.get('tipo') in RUN and d.get('hecho')]
    km=sum(num(d.get('dist')) or 0 for d in runs)
    suaves=[num(d.get('fcp')) for d in runs if d.get('tipo') in ('trote','fondo') and num(d.get('fcp'))]
    sue=[num(d.get('sue')) for d in dias if num(d.get('sue'))]
    E.append(kpis([(f'{len(hechos)}/{len(plan)}','sesiones hechas'),(f'{km:.1f}','km corridos'),
                   (f'{sum(suaves)/len(suaves):.0f}' if suaves else '—','pulso días suaves (meta ≤150)'),
                   (f'{sum(sue)/len(sue):.1f} h' if sue else '—','sueño promedio (meta ≥6.5)')]))
    E.append(Spacer(1,10))
    # cumplimiento por día
    row=[];row2=[]
    for i,d in enumerate(dias):
        col=OK if d.get('hecho') else (MUT if d.get('tipo')=='descanso' else WARN)
        mark='(sí)' if d.get('hecho') else ('' if d.get('tipo')=='descanso' else '(no)')
        row.append(Paragraph(f'<font name="Helvetica-Bold" color="{col}">{DIAS[i]} {mark}</font>',S(alignment=1,s=9)))
        row2.append(Paragraph(d.get('plan','')[:38],S(alignment=1,s=7,l=9,c=MUT)))
    t=Table([row,row2],colWidths=[170*mm/7]*7)
    t.setStyle(TableStyle([('BOX',(0,0),(-1,-1),0.6,colors.HexColor(BORDER)),('INNERGRID',(0,0),(-1,-1),0.4,colors.HexColor(HL)),('VALIGN',(0,0),(-1,-1),'TOP')]))
    E+= [Paragraph('Cumplimiento de la semana',H2),t,Spacer(1,4),Paragraph('(sí) hecha · (no) no registrada · vacío = descanso',SMALL),Spacer(1,8)]
    E.append(box(Paragraph('<font name="Helvetica-Bold" color="%s">Cómo leer este reporte</font><br/>Verde = vas bien, amarillo = cuidado con algo puntual, rojo = hay que cambiar el plan. Cada gráfico tiene debajo una explicación en palabras simples de qué significa para ti.'%PRI,P)))
    # ---- carrera ----
    E.append(Spacer(1,6)); E.append(Paragraph('Carrera',H2))
    if runs:
        lab=[f"{DIAS[dias.index(d)]}\n{d.get('plan','')[:14]}" for d in runs]
        fcp=[num(d.get('fcp')) or 0 for d in runs]; fcm=[num(d.get('fcm')) for d in runs]
        fig,ax=plt.subplots(figsize=(7.2,2.7))
        bars=ax.bar(lab,fcp,color=[OK if (v<=150 or r.get('tipo') in ('intervalos','ritmo')) else WARN for v,r in zip(fcp,runs)],width=0.35,label='Pulso promedio')
        if len(runs)<4: ax.set_xlim(-1.2,len(runs)+0.2)
        for b,v in zip(bars,fcp): ax.text(b.get_x()+b.get_width()/2,v+1,f'{v:.0f}',ha='center',fontsize=8,color=TXT)
        if any(fcm): ax.scatter(lab,[v or 0 for v in fcm],color=BAD,zorder=3,label='Pulso máximo',s=22)
        ax.axhline(150,ls='--',color=PRI,lw=1); ax.text(ax.get_xlim()[0]+0.05,151.5,'tope días suaves: 150',fontsize=7,color=PRI)
        ax.set_ylim(100,max([v or 0 for v in fcm]+fcp+[160])+12); ax.set_ylabel('ppm'); ax.legend(fontsize=7,frameon=False,loc='lower left')
        E.append(fig_img(fig)); E.append(Paragraph(A.get('txt_pulso',''),P)); E.append(Spacer(1,8))
        cad=[num(d.get('cad')) for d in runs]
        if any(cad):
            fig,ax=plt.subplots(figsize=(7.2,2.2)); ax.axhspan(165,170,color=SOFT,label='zona ideal 165-170')
            ax.plot(lab,[v if v else None for v in cad],marker='o',color=PRI,lw=2)
            for x,v in zip(lab,cad):
                if v: ax.text(x,v+1.2,f'{v:.0f}',ha='center',fontsize=8)
            ax.set_ylim(140,180); ax.set_ylabel('pasos/min')
            if len(runs)<4: ax.set_xlim(-1.2,len(runs)+0.2)
            ax.legend(fontsize=7,frameon=False,loc='lower left')
            E.append(fig_img(fig)); E.append(Paragraph(A.get('txt_cadencia',''),P))
    else:
        E.append(Paragraph('No hay carreras registradas esta semana.',P))
    # ---- fuerza ----
    E.append(Spacer(1,6)); E.append(Paragraph('Fuerza: abdominales militares y push-ups',H2))
    F=A.get('fuerza_hist')
    if F and F.get('semanas'):
        fig,axs=plt.subplots(1,2,figsize=(7.4,2.6))
        for ax,key,apr,meta,tt in [(axs[0],'abd',52,58,'Abd. militares (1\'30")'),(axs[1],'push',43,48,'Push-ups (1\'30")')]:
            xs=[f"S{s}" for s in F['semanas']]; ys=[v if v is not None else None for v in F.get(key,[])]
            xi=list(range(len(xs))); ax.plot(xi,[float('nan') if v is None else v for v in ys],marker='o',color=PRI,lw=2); ax.set_xticks(xi); ax.set_xticklabels(xs); ax.axhline(apr,ls='--',color=WARN,lw=1); ax.axhline(meta,ls='--',color=OK,lw=1)
            n=len(xs)-1; ax.text(n,apr-3.2,f'aprobar {apr}',fontsize=7,color=WARN,ha='right'); ax.text(n,meta+1,f'meta {meta}',fontsize=7,color=OK,ha='right')
            ax.set_title(tt,fontsize=9,color=TXT); ax.tick_params(axis='x',labelsize=7,rotation=45)
            vals=[v for v in ys if v is not None]; ax.set_ylim(min(vals+[apr])-10 if vals else 0,max(vals+[meta])+8)
        fig.tight_layout(); E.append(fig_img(fig))
    E.append(Paragraph(A.get('txt_fuerza',''),P))
    # ---- recuperación ----
    E.append(Paragraph('Recuperación',H2))
    if sue:
        fig,ax=plt.subplots(figsize=(7.2,2.1))
        vals=[num(d.get('sue')) or 0 for d in dias]
        ax.bar(DIAS,vals,color=[OK if v>=6.5 else (WARN if v>0 else HL) for v in vals],width=0.5)
        ax.axhline(6.5,ls='--',color=PRI,lw=1); ax.text(6.4,6.6,'mínimo 6.5 h',fontsize=7,color=PRI,ha='right'); ax.set_ylim(0,9); ax.set_ylabel('horas')
        E.append(fig_img(fig))
    rod=[(DIAS[i],num(d.get('rod'))) for i,d in enumerate(dias) if num(d.get('rod')) is not None]
    if rod:
        E.append(Paragraph('Rodilla: '+' · '.join(f'{a} <font name="Helvetica-Bold" color="{OK if v<3 else BAD}">{v:.0f}/10</font>' for a,v in rod),P))
    E.append(Paragraph(A.get('txt_recuperacion',''),P))
    # ---- ajustes ----
    aj=''.join(f'<font name="Helvetica-Bold" color="{PRI}">{i+1}.</font> {a}<br/><br/>' for i,a in enumerate(A.get('ajustes',[])))
    E.append(KeepTogether([Spacer(1,8),Paragraph('Ajustes para la próxima semana',H2),box(Paragraph(aj or 'Sin cambios.',P),bg='#F7FAFC')]))
    PS=A.get('plan_siguiente')
    if PS and PS.get('dias'):
        E.append(PageBreak())
        E.append(Paragraph('Tu plan de la próxima semana',H1)); E.append(Paragraph(PS.get('rango',''),PM)); E.append(Spacer(1,8))
        if PS.get('cambios'): E+= [box(Paragraph('<font name="Helvetica-Bold" color="%s">Qué cambia y por qué</font><br/>%s'%(PRI,PS['cambios']),P)),Spacer(1,10)]
        rows=[[Paragraph('<font name="Helvetica-Bold" color="white">Día</font>',S(s=9)),Paragraph('<font name="Helvetica-Bold" color="white">Sesión</font>',S(s=9)),Paragraph('<font name="Helvetica-Bold" color="white">Cambio</font>',S(s=9))]]
        for d in PS['dias']:
            ch=d.get('cambio','') or '='
            col=TXT if ch=='=' else PRI
            rows.append([Paragraph(f'<font name="Helvetica-Bold">{d.get("dia","")}</font>',S(s=9)),Paragraph(d.get('sesion',''),S(s=9,l=12)),Paragraph(f'<font color="{col}">{ch}</font>',S(s=8.5,l=11))])
        t=Table(rows,colWidths=[24*mm,96*mm,50*mm],repeatRows=1)
        t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor(PRI)),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.HexColor(HL)]),
          ('BOX',(0,0),(-1,-1),0.6,colors.HexColor(BORDER)),('INNERGRID',(0,0),(-1,-1),0.4,colors.HexColor(BORDER)),('VALIGN',(0,0),(-1,-1),'MIDDLE'),
          ('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6)]))
        E+= [t,Spacer(1,8),Paragraph('Esta semana ya está cargada en tu app. Si quieres cambiar algo, respóndeme en esta misma conversación (por ejemplo: "exígeme más en intervalos" o "el jueves no puedo").',SMALL)]
    if A.get('nota_strava'): E+= [Spacer(1,6),Paragraph(A['nota_strava'],SMALL)]
    E+= [Spacer(1,10),Paragraph('<font name="Helvetica-Bold">Glosario rápido</font> — <b>Pulso promedio</b>: qué tan fuerte trabajó tu corazón; en días suaves debe quedar en 150 o menos. <b>Cadencia</b>: pasos por minuto; más pasos y más cortos = menos impacto en la rodilla. <b>Readiness</b>: qué tan recuperado amaneces según el reloj (más alto = mejor). <b>RPE</b>: tu sensación de esfuerzo del 1 al 10.',SMALL)]
    doc.build(E)

if __name__=='__main__':
    A=json.load(open(sys.argv[1],encoding='utf-8')); out=sys.argv[2]; build(A,out)
    if subprocess.run(['which','qpdf'],capture_output=True).returncode==0:
        tmp=out+'.tmp'
        if subprocess.run(['qpdf','--recompress-flate','--compression-level=9','--object-streams=generate',out,tmp]).returncode==0: os.replace(tmp,out)
    print('PDF:',out,f'({os.path.getsize(out)//1024} KB)')
