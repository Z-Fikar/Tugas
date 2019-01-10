global img img_name Z i j c dir;

prompt = "Insert filter matrix Z: ";
Z = input(prompt);
[i,j] = size(Z);

if(validation())
    c = [ceil(i/2), ceil(j/2)];
    xStart = c(1) - 1;
    xEnd = c(1) - i;
    yStart = c(2) - 1;
    yEnd= c(2) - j;
    
    RES = img;
    [m,n,o] = size(RES);
    
    for x = 1:m
        for y = 1:n
            for z = 1:o
                if((x>=1+xStart && x<=m+xEnd) && (y>=1+yStart && y<=n+yEnd))
                    RES(x,y,z) = convolution(x,y,z);
                end
            end
        end
    end
    
    name_res = strcat(dir,"low_pass_",img_name);
    imwrite(uint8(RES), name_res);
    imshow(RES);
else
    disp("Validation error! All of Z's element have to be positive and Sum of them have to be equal to 1!");
end


function f = validation()
    global Z i j;
    total = 0;
    positive = true;
    
    for x = 1:i
        for y = 1:j
            if(Z(x,y)<=0)
                positive = false;
                break;
            end
            total = total+ Z(x,y);
        end
        if(~positive)
            break;
        end
    end
    
    if(positive)
        f = total == 1;
    else
        f = positive;
    end
end

function f = convolution(a,b,rgb)
    global img Z i j c;
    dx = a - c(1);
    dy = b - c(2);
    total = 0;
    
    for x = 1:i
        for y = 1:j
            total = total + Z(x,y) * img(x+dx, y+dy, rgb);
        end
    end
    
    f = total;
end