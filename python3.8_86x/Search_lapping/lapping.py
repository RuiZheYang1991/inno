    def testt(self):

        rname = []
        rno = []
        rseat = []
        rtime = []
        rio = []
        num = self.ui.user_number.toPlainText()
        start_date = self.ui.startDateEdit.dateTime()
        end_date = self.ui.endDateEdit.dateTime()

        str_start_date = start_date.toString('yyyyMMddHHmm00')
        str_end_date = end_date.toString('yyyyMMddHHmm00')

        # df0 = pd.read_sql(f"select * from OfficeCheckData where Time < 20210625182921", self.res)
        # print(df0)
        name=pd.read_sql(f"select * from OfficeCheckData where UserNo = {num} AND {str_start_date} < Time AND Time< {str_end_date} AND IO='O'", self.res)
        timE=pd.read_sql(f"select Time from OfficeCheckData where UserNo = {num} AND {str_start_date} < Time AND Time< {str_end_date} AND IO='O'", self.res)
        #print(timE.values)
        covid_time=timE.values
        buffer=2

        ng_seat=pd.read_sql(f"select Seat from OfficeCheckData where UserNo = {num} AND {str_start_date} < Time AND Time< {str_end_date} AND IO='O'", self.res)


        last_df=pd.DataFrame()
        # df=pd.concat([last_df,ng_seat],axis=0)
        # print(df)
        for i in covid_time:
            after=str(int(i[0])+buffer*1000)
            # print(i[0])
            # print(after)
            filteR=pd.read_sql(f"select * from OfficeCheckData where Time between {i[0]} AND {after} ", self.res)
            #print(type(filteR))

            last_df=pd.concat([last_df,filteR],axis=0)
        last_df=last_df[last_df["Seat"].notna()]
        get_ngseat=[x for i in ng_seat.values for x in i]
        print(get_ngseat)

        mask=last_df["Seat"].isin(get_ngseat)
        #print(mask)
        #
        last_df=last_df[mask]
        print(last_df.values)
        for d in last_df.values:
            
            self.ui.show_data.appendPlainText(f"{d[0]}  {d[1]}  {d[2]}  {d[3]}  {d[4]}")
