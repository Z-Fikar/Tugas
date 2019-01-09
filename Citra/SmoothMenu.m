global img;

Main();

function f = Main()
    global img
    [x,y,z] = size(img);
    if(x>1 & y>1 & z>=1)
        disp("==== Smoothing Filter ====");
        disp("1. Mean filter");
        disp("2. Low Pass filter");
        disp("3. Median filter");
        disp("0. Exit");
        disp("==========================");
        cmd = input("Command: ");
        options = [0 1 2 3];
        if(ismember(cmd,options))
            if(cmd == 1)
                Mean;
            elseif(cmd == 2)
                LowPass;
            elseif(cmd == 3)
                Median;
            end
        else
            disp("Command error!");
        end
    end
end
