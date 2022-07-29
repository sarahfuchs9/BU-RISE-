
#  Driver Program for Midbrain Dopaminergic Neuron model 
"""Different from dist.hoc by Ih current hd, # of  synapses, AMPA,NMDA formulation for all dend 0-37, inserting mechanisms in "forsec distDend"
 Prox or Distdend sections not in each dendrite, number of segments (inside each compartemnt) formulation nseg, read i.c. from different files,
print less dend data, writ i.c. in diferent file 

The following command loads the standard run library functions into
the simulator.  These library functions are used to initialize the
simulator, begin and end simulations, and plot variables during a
simulation. """

import matplotlib.pyplot as plt
from neuron import h
h.load_file("stdlib.hoc")
h.load_file("nrngui.hoc")
h.load_file("dopaminergic.hoc")
timecon = 0
back= 0 #  switch for running in the background 
sakmann=0
h.load_file("fixnseg.hoc")
if back != 1:
    h.load_file("nrngui.hoc")
verbose= 0 ## 0
h.v_init = -62.6
vcseries = 0
clamp = 0                     ##  switch for voltage clamp
restart = 0 ## 1 switch for initializing from state.old 
h("tstart = 0")
if(vcseries):
    h.tstop = 800 
else:
    h.tstop = 5000    ## time in msec
if clamp==1 and vcseries != 1:
    h.tstop= 600
if timecon==1 :
    h.tstop = 800


nsyn = 45			##  The number of synapses 
Dtmax = 1.0  
Dt = 1.00
if timecon==1:
    Dtmax = 1.0 
dt = 5e-1 ## 5e-4  
if timecon: 
    dt = 0.01
    
nainit=  4.075
vsolder=h.v_init
vsold=h.v_init

# PARAMETERS - adjusted per figure
na_cond =  550.0e-6 
kca_cond = 59.0e-6
iapl = 0 # in nA, -0.180nA=-180pA
idelay = 4000
idur = 1000

# PARAMETERS
kdr_cond = 665.0e-6
ca_cond = 11.196e-6
kca_cond = 59.0e-6
a_cond_s = 570.0e-6
a_cond_p = 285.0e-6
a_cond_d = 266.0e-6
# stronger gA *1.28 =  729.6, 364.8, 340.48

h("global_ra = 40")
h("forall Ra = global_ra")
h("global_cm = 1.0")
h("forall cm = global_cm")
g_celsius = 35
h.celsius = g_celsius
h('forall ion_style("na_ion", 2,2,0,0,0)')

# access soma	 # UNSURE IF NEEDED		#  All default references are to soma 

# objectvar vc # UNSURE IF NEEDED
h("objref cvode")
h("cvode = new CVode(0)") #  0 for clamp
h("x= cvode.active(0)")

stimobj = h.MyIClamp(h.soma[0](0.5))

def init_cell():
    global g_celsius, stimobj
    # First set all of the dimensions and 
    # insert the channels into each section
    
    
    for sec in h.soma:
    	sec.insert("nabalan")
    	sec.insert("hh3")
    	sec.insert("pump")
    	sec.insert("leak")
    	sec.insert("cabalan")
    	sec.insert("cachan")
    	sec.insert("kca")
    	for seg in sec:
            seg.hh3.gnabar = na_cond
            seg.hh3.gkhhbar = kdr_cond
            seg.hh3.gkabar = a_cond_s
            seg.hh3.qv = 56.0
            seg.hh3.qs = 8.0
    
            seg.cachan.gcalbar = ca_cond
            #seg.cachan.gkbar = 0.0
    
            seg.kca.gkbar = kca_cond
    
       
    stimobj.delay = idelay # ms, time after start of sim when you want the current injection to begin
    stimobj.dur = idur # ms, duration of current pulse
    stimobj.amp = 0 # nA, contains the level of current being injected at any given time during simulation   
    stimobj.amp2 = iapl # nA, contains the level of current being injected at any given time during simulation   
    # in nA, -0.180nA=-180pA
    
    
    for sec in h.proxDend:
    	sec.insert("nabalan")
    	sec.insert("hh3")
    	sec.insert("pump")
    	sec.insert("leak")
    	sec.insert("cabalan")
    	sec.insert("cachan")
    	sec.insert("kca")
    	for seg in sec:
            seg.hh3.gnabar = na_cond
            seg.hh3.gkhhbar = kdr_cond
            seg.hh3.gkabar = a_cond_p
            seg.hh3.qv = 60.0
            seg.hh3.qs = 5.0
    
            seg.cachan.gcalbar = ca_cond
            # seg.cachan.gkbar = 0.0
    
            seg.kca.gkbar = kca_cond
    
    
    for sec in h.distDend:
    	sec.insert("nabalan")
    	sec.insert("hh3")
    	sec.insert("pump")
    	sec.insert("leak")
    	sec.insert("cabalan")
    	sec.insert("cachan")
    	sec.insert("kca")
    
    	for seg in sec:
            seg.hh3.gnabar = na_cond
            seg.hh3.gkhhbar = kdr_cond
            seg.hh3.gkabar = a_cond_d
            seg.hh3.qv = 60.0
            seg.hh3.qs = 5.0
    
            seg.cachan.gcalbar = ca_cond
            # seg.cachan.gkbar = 0.0
    
            seg.kca.gkbar = kca_cond
    
    

    h("forall cm = global_cm")
    h("forall Ra = global_ra")
    g_celsius = 35


def updatecell():
    global g_celsius, stimobj
    # First set all of the dimensions and 
    # insert the channels into each section
    
    
    for sec in h.soma:
    	for seg in sec:
            seg.hh3.gnabar = na_cond
            seg.hh3.gkhhbar = kdr_cond
            seg.hh3.gkabar = a_cond_s
            seg.hh3.qv = 56.0
            seg.hh3.qs = 8.0
    
            seg.cachan.gcalbar = ca_cond
            #seg.cachan.gkbar = 0.0
    
            seg.kca.gkbar = kca_cond
    
       
    stimobj.delay = 2500 # ms, time after start of sim when you want the current injection to begin
    stimobj.dur = 2500 # ms, duration of current pulse
    stimobj.amp = 0 # nA, contains the level of current being injected at any given time during simulation   
    stimobj.amp2 = iapl # nA, contains the level of current being injected at any given time during simulation   
    # in nA, -0.180nA=-180pA
    
    
    for sec in h.proxDend:
    	for seg in sec:
            seg.hh3.gnabar = na_cond
            seg.hh3.gkhhbar = kdr_cond
            seg.hh3.gkabar = a_cond_p
            seg.hh3.qv = 60.0
            seg.hh3.qs = 5.0
    
            seg.cachan.gcalbar = ca_cond
            # seg.cachan.gkbar = 0.0
    
            seg.kca.gkbar = kca_cond
    
    
    for sec in h.distDend:    
    	for seg in sec:
            seg.hh3.gnabar = na_cond
            seg.hh3.gkhhbar = kdr_cond
            seg.hh3.gkabar = a_cond_d
            seg.hh3.qv = 60.0
            seg.hh3.qs = 5.0
    
            seg.cachan.gcalbar = ca_cond
            # seg.cachan.gkbar = 0.0
    
            seg.kca.gkbar = kca_cond
    
    

    h("forall cm = global_cm")
    h("forall Ra = global_ra")
    g_celsius = 35


def init():
    
    h("access soma")
    
    if restart == 0:
        h.finitialize(h.v_init)
        h.fcurrent()
    elif restart == 1:
        h('f1.ropen("state.old")')
        h('ss.fread(f1)')
        h('f1.close')
        h.finitialize(h.v_init)
        h('ss.restore()')
        h.t=h.tstart
        mm = h.cvode.active()
        if mm == 1:
            h("cvode.re_init()")
        else:
            h.fcurrent()
        h.frecord_init()
        
        h.t=h.tstart


def runandplot(figtitle):
    if back == 1:
        # if(!clamp ||verbose) {print t/1000,soma[1].v(0.5),soma[1].nai(0.5),soma[1].cai(0.5),dend[3].v(0.5),dend[3].cai(0.5),dend[17].v(0.5),dend[17].cai(0.5)}
        # if(clamp && !vcseries && !verbose) print t/1000,vc.i,soma.cai(0.5),soma.v(0.5)
        j = 10 if vcseries == 1 else 0
        
    
        if vcseries == 1:
            for i in range(j+1):
                h.vc.amp1 = h.vc.amp1 + 10      
            init()
            
        h("next = t + Dt")
        h("flag1=0")
        h("flag2=0")
        h("hold = 0")
        while h.t<h.tstop:
            h("vsolder=vsold")
            h("vsold=soma.v(0.5)")
            
            h.fadvance()
            if clamp == 0 or verbose == 1:
    
                if ((h.vsolder<h.vsold and h.soma[0].v(0.5) < h.vsold)
                    or (h.vsolder>h.vsold and h.soma[0].v(0.5)>h.vsold)):
                    h("vsolder=soma.v(0.5)")
                    # print t/1000,soma[1].v(0.5),soma[1].nai(0.5),soma[1].cai(0.5),dend[3].v(0.5),dend[3].cai(0.5),dend[17].v(0.5),dend[17].cai(0.5)
                    h("next = t + Dt")
                    h("flag2=1")
                    h("hold=dt")
                    h("soma.v(0.5)=vsolder")
                
    
            if h.t>=h.next:
                Dt = 100*dt
                if h.Dt>h.Dtmax:
                    h.Dt = h.Dtmax
                if h.Dt<.1:
                    h.Dt = .1
                h.next = h.t + h.Dt
                # if(!clamp||verbose) {print t/1000,soma[1].v(0.5),soma[1].nai(0.5),soma[1].cai(0.5),dend[3].v(0.5),dend[3].cai(0.5),dend[17].v(0.5),dend[17].cai(0.5)}
                # if(clamp && !vcseries && !verbose) print t/1000,vc.i,soma.cai(0.5),soma.v(0.5)
    
    
        
        # print t/1000,soma[1].v(0.5),soma[1].nai(0.5),soma[1].cai(0.5),dend[3].v(0.5),dend[3].cai(0.5),dend[17].v(0.5),dend[17].cai(0.5)
        # ifvcseries) print vc.amp1,vc.i
        h('f2.wopen("state.new")')
        h('ss.save()')
        h('ss.fwrite(f2)')
        h('f2.close')
        
    else:
        h("forall Ra = global_ra")
        h("forall cm = global_cm")
        h.celsius = g_celsius
    
    vvec = h.Vector().record(h.soma[0](0.5)._ref_v)
    tvec = h.Vector().record(h._ref_t)
    # ivec = h.Vector().record(stimobj._ref_i)
    h.tstop = 5000
    h.run()
    
    plt.figure()
    plt.plot(tvec, vvec, linewidth=2, label=str("soma[0](0.5) voltage"))
    plt.ylim([-80, 0])
    if fig[0] != '2':
        plt.xlim([1500, 3500])
    plt.title("Figure " + figtitle)
    plt.xlabel("Time (ms)")
    plt.ylabel("Membrane potential at soma (mV)")
    plt.show()


h("tot=0")
h("forall {tot=tot+nseg}")
print("segments before ", h.tot)
h("nseg=1")

#  Increase number of segments
h.geom_nseg()

h.tot=0
h("forall {tot=tot+nseg}")
print("segments after ", h.tot)

init_cell()	# Call the function to initialize our cell. 


print("Kuznetsova et al. 2010")

fig = input("Which figure do you want to run (or quit)? 2a2, 2b2, 2f2, or 6: ")

while fig[0].lower() != 'q':
    na_cond =  550.0e-6 
    kca_cond = 59.0e-6
    if fig[0] == '6':
        idelay = 2500
        idur = 2500
        
        ftype = input("Do you want dashed or solid? ")
        
        fig += ftype
        
        if ftype[0].lower() == 's':
            iapl = 0.1 # in nA, -0.180nA=-180pA   
        else:
            iapl = 0.5 # in nA, -0.180nA=-180pA
    else:
        idelay = 4000
        idur = 1000
        iapl = 0
        
        if fig.lower() == '2f2':
            na_cond = 0.0e-6
        if fig.lower() == '2b2':
            kca_cond = 0.0e-6
   
    updatecell()
    
    h("objref ss,f1,f2")
    h("ss = new SaveState()")
    h("f1 = new File()")
    h("f2 = new File()")
    
    init()
    runandplot(fig)
    fig = input("Which figure do you want to run (or quit)? 2a2, 2b2, 2f2, or 6: ")
