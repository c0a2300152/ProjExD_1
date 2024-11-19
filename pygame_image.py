import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))#スクリーンサーフェース
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img_r = pg.transform.flip(bg_img, True, False)
    kt_img = pg.image.load("fig/3.png")
    kt_img = pg.transform.flip(kt_img, True, False)

    kt_rct = kt_img.get_rect()
    kt_rct.center = 300, 200

    
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        
        key_lst = pg.key.get_pressed()#演習1(if文を削除)
        kt_rct.move_ip(-1, 0)
        if key_lst[pg.K_UP]:  # 上矢印キーが押されたら
            kt_rct.move_ip(0, -1)

        if key_lst[pg.K_DOWN]:  # 下矢印キーが押されたら
            kt_rct.move_ip(0, +1)
     
        if key_lst[pg.K_RIGHT]:  # 右矢印キーが押されたら
            kt_rct.move_ip(+1, 0)

        screen.blit(bg_img, [-tmr, 0])#貼り付けるメソッドが［blit]
        screen.blit(bg_img_r,[-tmr+1600, 0])

        screen.blit(bg_img, [-tmr+3200, 0])#貼り付けるメソッドが［blit]
        screen.blit(bg_img_r,[-tmr+4800, 0])

        screen.blit(kt_img, kt_rct)

 
        pg.display.update()
        tmr += 1        
        clock.tick(200)



if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()