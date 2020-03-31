set terminal gif animate delay 1
set output 'output.gif'
stats 'plot.dat' nooutput
set xrange [-2:2]
set yrange [-2:2]
unset key

do for [i=0:int(STATS_records)] {
   plot 'plot.dat' every ::::(i-1) w lp pt 12 ps 1  lc 2, 'plot.dat' every ::i::i pt 13 ps 2  lc 4
}

do for [i=0:50]{
    plot 'plot.dat' w lp pt 12 ps 1 lc 2
}