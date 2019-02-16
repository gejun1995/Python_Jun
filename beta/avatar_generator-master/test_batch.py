import identicon
def gen_avatar_batch(code,size):
	img= identicon.render_identicon(code, 100)
	#img.show()
	img.save('%s_%s.png'%(code,size))


x=330226199509302872
y=19950930
gen_avatar_batch(x,y )

