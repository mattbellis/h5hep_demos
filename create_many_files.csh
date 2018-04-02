@ i = 10

while ( $i < 30 )
    #foreach nevents ( 1000 10000 100000 )
    foreach nevents ( 100000 )

        set tag = `printf "%03d" $i`

        time python write_narrow_HEP_file_to_h5hep.py $nevents $tag

    end
    @ i += 1
end

@ i = 10

while ( $i < 30 )
    #foreach nevents ( 1000 10000 100000 )
    foreach nevents ( 100000 )

        set tag = `printf "%03d" $i`

        time python write_narrow_HEP_file_to_ROOT.py $nevents $tag

    end
    @ i += 1
end
