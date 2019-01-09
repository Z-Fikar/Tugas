global img img_name Z i j c dir;

prompt = "Insert filter matrix Z: ";
Z = input(prompt);
if(sum(Z,'all')==1)
    [i,j] = size(Z);
    
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
    disp("Sum of Z's element is not equal to 1!");
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