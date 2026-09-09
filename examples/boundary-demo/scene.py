"""Original teaching scene. No upstream 3Blue1Brown code or assets are copied."""
import json
import math
import textwrap
from pathlib import Path
import numpy as np
from manim import *

WORK=Path(__file__).resolve().parent
BEATS=json.loads((WORK/'timings.json').read_text(encoding='utf-8'))
BG='#10151D'; BLUE='#62B5E8'; GREEN='#62D6BD'; YELLOW='#F8D474'; ROSE='#F48C9E'; GRAY='#718093'
config.background_color=BG

def label(text, size=26, color=WHITE, width=12):
    obj=Text(text,font='Arial',font_size=size,color=color)
    if obj.width>width: obj.scale_to_fit_width(width)
    return obj

class BoundaryDemo(Scene):
    def construct(self):
        self.camera.background_color=BG
        gradient=ValueTracker(0)
        active=ValueTracker(0)
        origin=np.array([-3.15,-0.15,0.0]); scale=2.05
        def point(x,y=0): return origin+scale*np.array([x,y,0.0])
        def radius(x): return .4+gradient.get_value()*x
        def normal(): return np.array([-gradient.get_value(),math.sqrt(1-gradient.get_value()**2),0])
        def contact(x): return point(x)+scale*radius(x)*normal()
        def disk(x,color=GRAY,width=1.5): return Circle(radius=scale*radius(x),color=color,stroke_width=width).move_to(point(x))
        positions=np.linspace(-1,1,13)
        baseline=DashedLine(point(-1.2),point(1.2),color=GRAY,stroke_width=1.5)
        disks=always_redraw(lambda:VGroup(*[disk(x) for x in positions]))
        dots=VGroup(*[Dot(point(x),radius=.023,color=GRAY) for x in positions])
        central=Circle(radius=scale*.4,color=BLUE,stroke_width=4).move_to(origin)
        oldpoint=Dot(point(0,.4),radius=.065,color=ROSE)
        oldlabel=label('Original top',23,ROSE,width=2.4).move_to([-4.8,1.55,0])
        leader=Line(oldlabel.get_bottom(),oldpoint.get_center(),color=ROSE,stroke_width=1.5)
        legend=label('Blue: fixed disk    Pink: original point',21,width=6.3).move_to([-3,-2.22,0])
        note=label('Local illustration: selected disks from a continuous family\nAllowed regions, not probabilities',17.5,GRAY,width=12).move_to([0,2.72,0])
        self.add(note)
        divider=Line([.55,-2.45,0],[.55,2.25,0],color=GRAY,stroke_opacity=.3)
        panel=RoundedRectangle(width=5.45,height=4.35,corner_radius=.16,stroke_color=GRAY,stroke_opacity=.5).move_to([3.7,-.05,0])
        cue=label('Will it remain outside?',29,YELLOW,width=4.6).move_to([3.7,.4,0])
        cue2=label('Follow the same point.',24,GRAY,width=4.6).move_to([3.7,-.25,0])
        topedge=Line(point(-1.05,.4),point(1.05,.4),color=GREEN,stroke_width=4)
        # A fixed-magnification local patch, same mathematical coordinates as the main view.
        zoom_origin=np.array([3.55,-.15,0]); zoom_scale=14
        def zoom(x,y): return zoom_origin+zoom_scale*np.array([x+.025,y-.405,0])
        xs=np.linspace(-.16,.15,160)
        def arc(center,r): return [zoom(x,math.sqrt(r*r-(x-center)**2)) for x in xs]
        def curve(points,color,width=3):
            m=VMobject(stroke_color=color,stroke_width=width)
            m.set_points_as_corners(points); return m
        centralarc=curve(arc(0,.4),BLUE)
        neighborarc=curve(arc(.125,.4375),GREEN)
        patch=curve(arc(.125,.4375)+[zoom(.15,.31),zoom(-.16,.31),arc(.125,.4375)[0]],GREEN,0)
        patch.set_fill(GREEN,opacity=.12)
        zoomold=Dot(zoom(0,.4),radius=.067,color=ROSE)
        zoomtitle=label('Same point, magnified',24,width=4.7).move_to([3.7,1.73,0])
        zoomnote=label('Fixed magnification throughout',18,GRAY,width=4.7).move_to([3.7,-1.88,0])
        neighbor=Circle(radius=scale*.4375,color=GREEN,stroke_width=3).move_to(point(.125))
        zoomlabel=label('Inside the neighbor',22,ROSE,width=4.4).move_to([3.7,-1.4,0])
        envelope=always_redraw(lambda:Line(contact(-.92),contact(.92),color=GREEN,stroke_width=4.5))
        contactdot=always_redraw(lambda:Dot(contact(active.get_value()),color=GREEN,radius=.067))
        outward=always_redraw(lambda:Arrow(contact(active.get_value()),contact(active.get_value())+.65*normal(),color=YELLOW,buff=.025,stroke_width=4))
        activecircle=always_redraw(lambda:disk(active.get_value(),GREEN,3))
        zoomcontact=Dot(zoom(-.12,.4*math.sqrt(.91)),radius=.063,color=GREEN)
        # The envelope has normal (-g,sqrt(1-g*g)); y=(r0+g*x)/sqrt(1-g*g).
        zoomedge=curve([zoom(x,(.4+.3*x)/math.sqrt(.91)) for x in xs],GREEN,3.2)
        title=None; subtitle=None
        def beat(index,action):
            nonlocal title,subtitle
            data=BEATS[index]
            if title is not None:self.remove(title,subtitle)
            title=label(data['title'],35,width=12.3).move_to([0,3.35,0])
            subtitle=label('\n'.join(textwrap.wrap(data['text'],width=98)),23,width=12.3).move_to([0,-3.05,0])
            self.add(title,subtitle)
            start=self.time
            action()
            remainder=data['duration']-(self.time-start)
            if remainder < -.05:raise ValueError(f'Beat {index} actions exceed measured audio budget')
            if remainder>0:self.wait(remainder)
        def first():
            self.play(Create(baseline),FadeIn(disks),FadeIn(dots),Create(central),run_time=2)
            self.play(FadeIn(oldpoint),FadeIn(oldlabel),Create(leader),FadeIn(legend),Create(divider),Create(panel),FadeIn(cue),FadeIn(cue2),run_time=2)
            self.play(Indicate(oldpoint,color=ROSE),run_time=1)
        beat(0,first)
        def equal():
            self.play(Create(topedge),run_time=2)
            self.play(Transform(cue,label('Equal radii',30,GREEN,width=4.5).move_to(cue)),Transform(cue2,label('One common upper edge',24,width=4.6).move_to(cue2)),run_time=1)
        beat(1,equal)
        def growing():
            self.play(FadeOut(topedge),FadeOut(cue),FadeOut(cue2),gradient.animate.set_value(.3),run_time=3.5)
            self.play(Create(neighbor),FadeIn(zoomtitle),FadeIn(zoomnote),FadeIn(patch),Create(centralarc),Create(neighborarc),FadeIn(zoomold),run_time=2)
        beat(2,growing)
        def covered():
            self.play(FadeIn(zoomlabel),Indicate(zoomold,color=ROSE),run_time=1.8)
            self.play(Indicate(neighborarc,color=GREEN),run_time=1.2)
        beat(3,covered)
        def corrected():
            self.play(FadeOut(neighbor),FadeOut(zoomlabel),Create(envelope),run_time=1.8)
            self.play(FadeIn(contactdot),GrowArrow(outward),FadeIn(zoomcontact),Create(zoomedge),run_time=2)
            self.play(Indicate(zoomcontact,color=GREEN),run_time=1)
        beat(4,corrected)
        trail=VGroup()
        def follow():
            self.play(FadeIn(activecircle),run_time=.5)
            for value in [-.6,-.3,0,.3,.6]:
                self.play(active.animate.set_value(value),run_time=.8)
                mark=Dot(contact(value),color=GREEN,radius=.045)
                trail.add(mark); self.add(mark)
                self.wait(.2)
        beat(5,follow)
        def end():
            self.play(FadeOut(VGroup(patch,centralarc,neighborarc,zoomold,zoomtitle,zoomnote,zoomcontact,zoomedge)),run_time=1)
            words=VGroup(label('Position + outward direction',27,YELLOW,width=4.9),label('Propagate candidates',25,width=4.7),label('Keep the visible outer edge',24,GREEN,width=4.9)).arrange(DOWN,buff=.38).move_to([3.7,.2,0])
            self.play(FadeIn(words),active.animate.set_value(0),run_time=1.5)
        beat(6,end)
