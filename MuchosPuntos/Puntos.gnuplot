set terminal gif animate delay 1
set output 'output.gif'
stats 'plot.dat' nooutput
set xrange [-2:2]
set yrange [-2:2]
unset key

do for [i=0:int((STATS_records)/100)] {
   plot 'plot.dat' every ::::((100*i)-1) pt 12 ps 1  lc 2, 'plot.dat' every 100::::((100*i)) pt 12 ps 1  lc 3, 'plot.dat' every ::(100*i)::(100*i) pt 13 ps 2  lc 4
}

do for [i=0:50]{
    plot 'plot.dat' pt 12 ps 1 lc 2, 'plot.dat' every 100::::(STATS_records) pt 12 ps 1 lc 3
}