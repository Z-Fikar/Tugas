global img img_name dir;
dir = "Images/";
Main();

function f = Main()
    disp("==== Smoothing Program ====");
    disp("1. Save image from url");
    disp("2. Read image from folder");
    disp("0. Exit");
    disp("==========================");
    cmd = input("Command: ");
    options = [0 1 2];
    if(ismember(cmd,options))
        if(cmd == 1)
            SaveFromUrl();
        elseif(cmd == 2)
            ReadFromFolder();
        end
    else
        disp("Command error!");
    end
end
    
function f = SaveFromUrl()
    global img img_name dir;
    url = input("URL to image: ", 's');
    img = imread(url);
    splitted = split(url, "/");
    img_name = string(splitted(length(splitted)));
    imwrite(uint8(img), dir+img_name);
    imshow(img);
end

function f = ReadFromFolder()
    global img img_name dir;
    img_name = input("Image's name: ", 's');
    
    img = imread(dir+img_name);
    imshow(img);
end