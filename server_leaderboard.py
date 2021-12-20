
    @commands.command(aliases = ['lb'])
    async def leaderboard(self,ctx):
        """Have a look at the local charts of Economy"""
        bg = Image.open("./Assets/server_lb.png")
        font = ImageFont.truetype("./Assets/bahnschrift.ttf",size=13)
        font_big = ImageFont.truetype("./Assets/bahnschrift.ttf",size=25)
        
        x,x1,y,y_ = 90,400, 90, 66
        tops = {}
        for i in ctx.guild.members:
            money = await self.get(i.id)
            if money:
                tops[i.id]=money[1]

        tops = sorted(tops.items(),reverse=True)#For Descending list of Top charts

        draw = ImageDraw.Draw(bg)

        counter=10
        for i in tops:
            id,money = i[0],i[1]
            user = self.bot.get_user(id)
            name = f"{user.name.title()[:20]}.." if len(str(user.name))>20 else user.name.title()
            name = f"{user.name.title()[:20]}.." if len(str(user.name))>20 else user.name.title()
            draw.text((x,y),name,fill = (255,255,255),font=font_big)
            draw.text((x1,y),str(money),fill = (255,255,255),font=font_big)
            y+=y_
            counter-=1
            if counter==0:
                break
        while counter>0:
            draw.text((x,y),"    -    ",fill=(255,255,255))
            draw.text((x1,y),"    -    ",fill=(255,255,255))
            y+=y_
            counter-=1
        
        with BytesIO() as a:
            bg.save(a, 'PNG')
            a.seek(0)
            await ctx.send(file = discord.File(a, filename = "leader.png"))

