# Makefile for SoapBox social media manager
#          ___________
#         /          /|
#        /          / |
#       ------------  |
#       |    __    |  |
#       |   /  \   |  |
#       |   \__    |  |
#       |      \   |  |
#       |   \__/oap| / 
#       |          |/  
#       ------------   
#       
default: soap
CPP = g++
BUILDDIR = build

OBJS = 

soap: $(OBJS)
	$(CPP) -o soap $(OBJS)

clean:
	rm -r $(BUILDDIR)
	rm soap

