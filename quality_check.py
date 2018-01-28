class MrpQualityCheck(models.Model):
    _name = 'quality.check'
    _description = 'Quality Check'

    @api.depends('measure','x_length02','x_length03','x_length04','x_length05','x_length06','x_length07','x_length08',
                    'x_length09','x_length10','x_length11','x_length12','x_length13','x_length14','x_length15',
                    'x_length16','x_length17','x_length18','x_length19','x_length20')
    def x_min_measured_length(self):
        for record in self:
          record['x_min_measured_length'] = min(self.measure,self.x_length02,
                                              self.x_length03,self.x_length04,
                                              self.x_length05,self.x_length06,
                                              self.x_length07,self.x_length08,
                                              self.x_length09,self.x_length10,
                                              self.x_length11,self.x_length12,
                                              self.x_length13,self.x_length14,
                                              self.x_length15,self.x_length16,
                                              self.x_length17,self.x_length18,
                                              self.x_length19,self.x_length20, key=lambda x:(x==0, x))

    @api.depends('measure','x_length02','x_length03','x_length04','x_length05','x_length06','x_length07','x_length08',
                   'x_length09','x_length10','x_length11','x_length12','x_length13','x_length14','x_length15',
                   'x_length16','x_length17','x_length18','x_length19','x_length20')
    def x_max_measured_length(self):
        for record in self:
          record['x_max_measured_length'] = max(self.measure,self.x_length02,
                                              self.x_length03,self.x_length04,
                                              self.x_length05,self.x_length06,
                                              self.x_length07,self.x_length08,
                                              self.x_length09,self.x_length10,
                                              self.x_length11,self.x_length12,
                                              self.x_length13,self.x_length14,
                                              self.x_length15,self.x_length16,
                                              self.x_length17,self.x_length18,
                                              self.x_length19,self.x_length20)

    @api.depends('x_perp01','x_perp02','x_perp03','x_perp04','x_perp05','x_perp06','x_perp07','x_perp08',
                   'x_perp09','x_perp10')
    def x_max_measured_perp(self):
        for record in self:
            record['x_max_measured_perp'] = max(self.x_perp01,self.x_perp02,self.x_perp03,
                                                self.x_perp04,self.x_perp05,self.x_perp06,
                                                self.x_perp07,self.x_perp08,self.x_perp09,self.x_perp10)

    @api.depends('x_height01','x_height02','x_height03','x_height04','x_height05')
    def x_min_height(self):
        for record in self:
            record['x_min_height']= min(self.x_height01,self.x_height02,self.x_height03,
                                        self.x_height04,self.x_height05,key=lambda x:(x==0, x))

    @api.depends('x_height01','x_height02','x_height03','x_height04','x_height05')
    def x_max_height(self):
        for record in self:
            record['x_max_height']= max(self.x_height01,self.x_height02,self.x_height03,
                                        self.x_height04,self.x_height05)

    @api.depends('x_pleats01','x_pleats02','x_pleats03','x_pleats04','x_pleats05')
    def x_min_pleats(self):
        for record in self:
            record['x_min_pleats'] = min(self.x_pleats01,self.x_pleats02,self.x_pleats03,
                                        self.x_pleats04,self.x_pleats05, key=lambda x:(x==0, x))

    @api.depends('x_pleats01','x_pleats02','x_pleats03','x_pleats04','x_pleats05')
    def x_max_pleats(self):
        for record in self:
            record['x_max_pleats'] = max(self.x_pleats01,self.x_pleats02,self.x_pleats03,
                                        self.x_pleats04,self.x_pleats05)

    @api.depends('x_width01','x_width02','x_width03','x_width04','x_width05')
    def x_min_width(self):
        for record in self:
            record['x_min_width'] = min(self.x_width01,self.x_width02,self.x_width03,
                                        self.x_width04,self.x_width05, key=lambda x:(x==0, x))

    @api.depends('x_width01','x_width02','x_width03','x_width04','x_width05')
    def x_max_width(self):
        for record in self:
            record['x_max_width'] = max(self.x_width01,self.x_width02,self.x_width03,
                                        self.x_width04,self.x_width05)

    @api.depends('x_qty_production','workcenter_id')
    def x_qty_inspection(self):
        for record in self:
            if self.x_qty_production*.1 >= 10 and self.workcenter_id.id == 5:
                record['x_qty_inspection']=10
                self.write({'x_qty_inspection_stored': 10})
                record['x_qty_inspection_stored']=10
            elif self.x_qty_production*.1 >= 20 and self.workcenter_id.id == 2:
                record['x_qty_inspection']=20
                self.write({'x_qty_inspection_stored': 20})
                record['x_qty_inspection_stored']=20
            elif self.x_qty_production/30*.1 >= 5 and self.workcenter_id.id == 1:
                record['x_qty_inspection']=5
                self.write({'x_qty_inspection_stored': 5})
                record['x_qty_inspection_stored']=5
            elif (self.x_qty_production/30*.1 < 5 and self.x_qty_production/30*.1 > 1
            and self.workcenter_id.id == 1):
                record['x_qty_inspection']=round(self.x_qty_production/30*.1)
                self.write({'x_qty_inspection_stored': round(self.x_qty_production/30*.1)})
                record['x_qty_inspection_stored']=round(self.x_qty_production/30*.1)
            elif self.x_qty_production/30*.1 <= 1 and self.workcenter_id.id == 1:
                record['x_qty_inspection']=1
                self.write({'x_qty_inspection_stored': 1})
                record['x_qty_inspection_stored']=1
            elif self.x_qty_production*.1 <= 1 and self.workcenter_id.id != 1:
                record['x_qty_inspection']=1
                self.write({'x_qty_inspection_stored': 1})
                record['x_qty_inspection_stored']=1
            elif self.workcenter_id.id != 1:
                record['x_qty_inspection']=round(self.x_qty_production*.1)
                self.write({'x_qty_inspection_stored': round(self.x_qty_production*.1)})
                record['x_qty_inspection_stored']=round(self.x_qty_production*.1)

    @api.depends('x_min_measured_length','x_tolerance_min','x_max_measured_length','x_tolerance_max')
    def x_length_fail(self):
        for record in self:
          if self.x_min_measured_length > 0:
              if (self.x_min_measured_length < self.x_tolerance_min or
                  self.x_max_measured_length > self.x_tolerance_max):
                  record['x_length_fail']="FAIL"

    @api.depends('x_min_measured_length','x_tolerance_min','x_max_measured_length','x_tolerance_max')
    def x_length_pass(self):
        for record in self:
          if (self.x_min_measured_length >= self.x_tolerance_min and
              self.x_max_measured_length <= self.x_tolerance_max):
              record['x_length_pass']="PASS"

    @api.depends('x_max_measured_perp','x_perp_max_tol')
    def x_perp_fail(self):
        for record in self:
            if self.x_max_measured_perp > self.x_perp_max_tol:
                record['x_perp_fail']="FAIL"

    @api.depends('x_max_measured_perp','x_perp_max_tol')
    def x_perp_pass(self):
        for record in self:
            if self.x_max_measured_perp >= 1 and self.x_max_measured_perp <= self.x_perp_max_tol:
                record['x_perp_pass']="PASS"

    @api.depends('x_min_height','x_max_height','x_height_min_tol','x_height_max_tol')
    def x_height_fail(self):
        for record in self:
            if self.x_min_height > 0:
                if (self.x_min_height < self.x_height_min_tol or
                    self.x_max_height > self.x_height_max_tol):
                    record['x_height_fail']="FAIL"

    @api.depends('x_min_height','x_max_height','x_height_min_tol','x_height_max_tol')
    def x_height_pass(self):
        for record in self:
            if (self.x_min_height >= self.x_height_min_tol and
                self.x_max_height <= self.x_height_max_tol):
                record['x_height_pass']="PASS"

    @api.depends('x_min_pleats','x_max_pleats','x_pleats_min_tol','x_pleats_max_tol')
    def x_pleats_fail(self):
        for record in self:
            if self.x_min_pleats > 0:
                if (self.x_min_pleats < self.x_pleats_min_tol or
                    self.x_max_pleats > self.x_pleats_max_tol):
                    record['x_pleats_fail']="FAIL"

    @api.depends('x_min_pleats','x_max_pleats','x_pleats_min_tol','x_pleats_max_tol')
    def x_pleats_pass(self):
        for record in self:
            if (self.x_min_pleats >= self.x_pleats_min_tol and
                self.x_max_pleats <= self.x_pleats_max_tol):
                record['x_pleats_pass']="PASS"

    @api.depends('x_min_width','x_max_width','x_width_min_tol','x_width_max_tol')
    def x_width_fail(self):
        for record in self:
            if self.x_min_width > 0:
                if (self.x_min_width < self.x_width_min_tol or
                    self.x_max_width > self.x_width_max_tol):
                    record['x_width_fail']="FAIL"

    @api.depends('x_min_width','x_max_width','x_width_min_tol','x_width_max_tol')
    def x_width_pass(self):
        for record in self:
            if (self.x_min_width >= self.x_width_min_tol and
                self.x_max_width <= self.x_width_max_tol):
                record['x_width_pass']="PASS"

    @api.depends('workcenter_id','x_seal_in_place','x_passed_visual_inspection','x_qty_inspection_stored','x_perp01','x_perp02',
                    'x_perp03','x_perp04','x_perp05','x_perp06','x_perp07','x_perp08','x_perp09','x_perp10','measure','x_length02',
                    'x_length03','x_length04','x_length05','x_length06','x_length07','x_length08','x_length09','x_length10',
                    'x_length11','x_length12','x_length13','x_length14','x_length15','x_length16','x_length17','x_length18',
                    'x_length19','x_length20','x_height01','x_height02','x_height03','x_height04','x_height05','x_pleats01',
                    'x_pleats02','x_pleats03','x_pleats04','x_pleats05','x_product_material','x_width01','x_width02',
                    'x_width03','x_width04','x_width05')
    def x_check_complete(self):
        for record in self:
            if (self.x_seal_in_place == True and self.x_passed_visual_inspection == True
            and self.workcenter_id.id == 5):
                if self.x_qty_inspection_stored == 1 and self.x_perp01 > 0 and self.measure > 0:
                    record['x_check_complete']=True
                    self.write({'x_check_complete_stored': True})
                    record['x_check_complete_stored']=True
                elif (self.x_qty_inspection_stored == 2 and self.x_perp01 > 0 and self.x_perp02 > 0
                and self.measure > 0 and self.x_length02 > 0):
                    record['x_check_complete']=True
                    self.write({'x_check_complete_stored': True})
                    record['x_check_complete_stored']=True
                elif (self.x_qty_inspection_stored == 3 and self.x_perp01 > 0 and self.x_perp02 > 0
                and self.x_perp03 > 0 and self.measure > 0 and self.x_length02 > 0 and self.x_length03 > 0):
                    record['x_check_complete']=True
                    self.write({'x_check_complete_stored': True})
                    record['x_check_complete_stored']=True
                elif (self.x_qty_inspection_stored == 4 and self.x_perp01 > 0 and self.x_perp02 > 0
                and self.x_perp03 > 0 and self.x_perp04 > 0 and self.measure > 0 and self.x_length02 > 0
                and self.x_length03 > 0 and self.x_length04 > 0):
                    record['x_check_complete']=True
                    self.write({'x_check_complete_stored': True})
                    record['x_check_complete_stored']=True
                elif (self.x_qty_inspection_stored == 5 and self.x_perp01 > 0 and self.x_perp02 > 0
                and self.x_perp03 > 0 and self.x_perp04 > 0 and self.x_perp05 > 0 and self.measure > 0
                and self.x_length02 > 0 and self.x_length03 > 0 and self.x_length04 > 0
                and self.x_length05 > 0):
                    record['x_check_complete']=True
                    self.write({'x_check_complete_stored': True})
                    record['x_check_complete_stored']=True
                elif (self.x_qty_inspection_stored == 6 and self.x_perp01 > 0 and self.x_perp02 > 0
                and self.x_perp03 > 0 and self.x_perp04 > 0 and self.x_perp05 > 0 and self.x_perp06 > 0
                and self.measure > 0 and self.x_length02 > 0 and self.x_length03 > 0 and self.x_length04 > 0
                and self.x_length05 > 0 and self.x_length06 > 0):
                    record['x_check_complete']=True
                    self.write({'x_check_complete_stored': True})
                    record['x_check_complete_stored']=True
                elif (self.x_qty_inspection_stored == 7 and self.x_perp01 > 0 and self.x_perp02 > 0
                and self.x_perp03 > 0 and self.x_perp04 > 0 and self.x_perp05 > 0 and self.x_perp06 > 0
                and self.x_perp07 > 0 and self.measure > 0 and self.x_length02 > 0 and self.x_length03 > 0
                and self.x_length04 > 0 and self.x_length05 > 0 and self.x_length06 > 0 and self.x_length07 > 0):
                    record['x_check_complete']=True
                    self.write({'x_check_complete_stored': True})
                    record['x_check_complete_stored']=True
                elif (self.x_qty_inspection_stored == 8 and self.x_perp01 > 0 and self.x_perp02 > 0
                and self.x_perp03 > 0 and self.x_perp04 > 0 and self.x_perp05 > 0 and self.x_perp06 > 0
                and self.x_perp07 > 0 and self.x_perp08 > 0 and self.measure > 0 and self.x_length02 > 0
                and self.x_length03 > 0 and self.x_length04 > 0 and self.x_length05 > 0 and self.x_length06 > 0
                and self.x_length07 > 0 and self.x_length08 > 0):
                    record['x_check_complete']=True
                    self.write({'x_check_complete_stored': True})
                    record['x_check_complete_stored']=True
                elif (self.x_qty_inspection_stored == 9 and self.x_perp01 > 0 and self.x_perp02 > 0
                and self.x_perp03 > 0 and self.x_perp04 > 0 and self.x_perp05 > 0 and self.x_perp06 > 0
                and self.x_perp07 > 0 and self.x_perp08 > 0 and self.x_perp09 > 0 and self.measure > 0
                and self.x_length02 > 0 and self.x_length03 > 0 and self.x_length04 > 0
                and self.x_length05 > 0 and self.x_length06 > 0 and self.x_length07 > 0
                and self.x_length08 > 0 and self.x_length09 > 0):
                    record['x_check_complete']=True
                    self.write({'x_check_complete_stored': True})
                    record['x_check_complete_stored']=True
                elif (self.x_qty_inspection_stored == 10 and self.x_perp01 > 0 and self.x_perp02 > 0
                and self.x_perp03 > 0 and self.x_perp04 > 0 and self.x_perp05 > 0 and self.x_perp06 > 0
                and self.x_perp07 > 0 and self.x_perp08 > 0 and self.x_perp09 > 0 and self.x_perp10 > 0
                and self.measure > 0 and self.x_length02 > 0 and self.x_length03 > 0 and self.x_length04 > 0
                and self.x_length05 > 0 and self.x_length06 > 0 and self.x_length07 > 0
                and self.x_length08 > 0 and self.x_length09 > 0 and self.x_length10 > 0):
                    record['x_check_complete']=True
                    self.write({'x_check_complete_stored': True})
                    record['x_check_complete_stored']=True
                else:
                    record['x_check_complete']=False
                    self.write({'x_check_complete_stored': False})
                    record['x_check_complete_stored']=False
            elif self.workcenter_id.id == 1 and self.x_product_material == 'metal':
                if self.x_qty_inspection_stored == 1 and self.x_height01 > 0 and self.x_pleats01 > 0:
                    record['x_check_complete']=True
                    self.write({'x_check_complete_stored': True})
                    record['x_check_complete_stored']=True
                elif (self.x_qty_inspection_stored == 2 and self.x_height01 > 0 and self.x_height02 > 0
                and self.x_pleats01 > 0 and self.x_pleats02 > 0):
                    record['x_check_complete']=True
                    self.write({'x_check_complete_stored': True})
                    record['x_check_complete_stored']=True
                elif (self.x_qty_inspection_stored == 3 and self.x_height01 > 0 and self.x_height02 > 0
                and self.x_height03 > 0 and self.x_pleats01 > 0 and self.x_pleats02 > 0
                and self.x_pleats03 > 0):
                    record['x_check_complete']=True
                    self.write({'x_check_complete_stored': True})
                    record['x_check_complete_stored']=True
                elif (self.x_qty_inspection_stored == 4 and self.x_height01 > 0 and self.x_height02 > 0
                and self.x_height03 > 0 and self.x_height04 > 0 and self.x_pleats01 > 0
                and self.x_pleats02 > 0 and self.x_pleats03 > 0 and self.x_pleats04 > 0):
                    record['x_check_complete']=True
                    self.write({'x_check_complete_stored': True})
                    record['x_check_complete_stored']=True
                elif (self.x_qty_inspection_stored == 5 and self.x_height01 > 0 and self.x_height02 > 0
                and self.x_height03 > 0 and self.x_height04 > 0 and self.x_height05 > 0
                and self.x_pleats01 > 0 and self.x_pleats02 > 0 and self.x_pleats03 > 0
                and self.x_pleats04 > 0 and self.x_pleats05 > 0):
                    record['x_check_complete']=True
                    self.write({'x_check_complete_stored': True})
                    record['x_check_complete_stored']=True
                else:
                    record['x_check_complete']=False
                    self.write({'x_check_complete_stored': False})
                    record['x_check_complete_stored']=False
            elif self.workcenter_id.id == 1 and self.x_product_material == 'nylon':
                if self.x_qty_inspection_stored == 1 and self.x_height01 > 0 and self.x_width01 > 0:
                    record['x_check_complete']=True
                    self.write({'x_check_complete_stored': True})
                    record['x_check_complete_stored']=True
                elif (self.x_qty_inspection_stored == 2 and self.x_height01 > 0 and self.x_height02 > 0
                and self.x_width01 > 0 and self.x_width02 > 0):
                    record['x_check_complete']=True
                    self.write({'x_check_complete_stored': True})
                    record['x_check_complete_stored']=True
                elif (self.x_qty_inspection_stored == 3 and self.x_height01 > 0 and self.x_height02 > 0
                and self.x_height03 > 0 and self.x_width01 > 0 and self.x_width02 > 0
                and self.x_width03 > 0):
                    record['x_check_complete']=True
                    self.write({'x_check_complete_stored': True})
                    record['x_check_complete_stored']=True
                elif (self.x_qty_inspection_stored == 4 and self.x_height01 > 0 and self.x_height02 > 0
                and self.x_height03 > 0 and self.x_height04 > 0 and self.x_width01 > 0
                and self.x_width02 > 0 and self.x_width03 > 0 and self.x_width04 > 0):
                    record['x_check_complete']=True
                    self.write({'x_check_complete_stored': True})
                    record['x_check_complete_stored']=True
                elif (self.x_qty_inspection_stored == 5 and self.x_height01 > 0 and self.x_height02 > 0
                and self.x_height03 > 0 and self.x_height04 > 0 and self.x_height05 > 0
                and self.x_width01 > 0 and self.x_width02 > 0 and self.x_width03 > 0
                and self.x_width04 > 0 and self.x_width05 > 0):
                    record['x_check_complete']=True
                    self.write({'x_check_complete_stored': True})
                    record['x_check_complete_stored']=True
                else:
                    record['x_check_complete']=False
                    self.write({'x_check_complete_stored': False})
                    record['x_check_complete_stored']=False
            elif self.workcenter_id.id == 2:
                if self.x_qty_inspection_stored == 1 and self.measure > 0:
                    record['x_check_complete']=True
                    self.write({'x_check_complete_stored': True})
                    record['x_check_complete_stored']=True
                elif (self.x_qty_inspection_stored == 2 and self.measure > 0
                and self.x_length02 > 0):
                    record['x_check_complete']=True
                    self.write({'x_check_complete_stored': True})
                    record['x_check_complete_stored']=True
                elif (self.x_qty_inspection_stored == 3 and self.measure > 0
                and self.x_length02 > 0 and self.x_length03 > 0):
                    record['x_check_complete']=True
                    self.write({'x_check_complete_stored': True})
                    record['x_check_complete_stored']=True
                elif (self.x_qty_inspection_stored == 4 and self.measure > 0
                and self.x_length02 > 0 and self.x_length03 > 0
                and self.x_length04 > 0):
                    record['x_check_complete']=True
                    self.write({'x_check_complete_stored': True})
                    record['x_check_complete_stored']=True
                elif (self.x_qty_inspection_stored == 5 and self.measure > 0
                and self.x_length02 > 0 and self.x_length03 > 0 and self.x_length04 > 0
                and self.x_length05 > 0):
                    record['x_check_complete']=True
                    self.write({'x_check_complete_stored': True})
                    record['x_check_complete_stored']=True
                elif (self.x_qty_inspection_stored == 6 and self.measure > 0
                and self.x_length02 > 0 and self.x_length03 > 0 and self.x_length04 > 0
                and self.x_length05 > 0 and self.x_length06 > 0):
                    record['x_check_complete']=True
                    self.write({'x_check_complete_stored': True})
                    record['x_check_complete_stored']=True
                elif (self.x_qty_inspection_stored == 7 and self.measure > 0
                and self.x_length02 > 0 and self.x_length03 > 0 and self.x_length04 > 0
                and self.x_length05 > 0 and self.x_length06 > 0
                and self.x_length07 > 0):
                    record['x_check_complete']=True
                    self.write({'x_check_complete_stored': True})
                    record['x_check_complete_stored']=True
                elif (self.x_qty_inspection_stored == 8 and self.measure > 0
                and self.x_length02 > 0 and self.x_length03 > 0 and self.x_length04 > 0
                and self.x_length05 > 0 and self.x_length06 > 0 and self.x_length07 > 0
                and self.x_length08 > 0):
                    record['x_check_complete']=True
                    self.write({'x_check_complete_stored': True})
                    record['x_check_complete_stored']=True
                elif (self.x_qty_inspection_stored == 9 and self.measure > 0
                and self.x_length02 > 0 and self.x_length03 > 0 and self.x_length04 > 0
                and self.x_length05 > 0 and self.x_length06 > 0 and self.x_length07 > 0
                and self.x_length08 > 0 and self.x_length09 > 0):
                    record['x_check_complete']=True
                    self.write({'x_check_complete_stored': True})
                    record['x_check_complete_stored']=True
                elif (self.x_qty_inspection_stored == 10 and self.measure > 0
                and self.x_length02 > 0 and self.x_length03 > 0 and self.x_length04 > 0
                and self.x_length05 > 0 and self.x_length06 > 0 and self.x_length07 > 0
                and self.x_length08 > 0 and self.x_length09 > 0
                and self.x_length10 > 0):
                    record['x_check_complete']=True
                    self.write({'x_check_complete_stored': True})
                    record['x_check_complete_stored']=True
                elif (self.x_qty_inspection_stored == 11 and self.measure > 0
                and self.x_length02 > 0 and self.x_length03 > 0 and self.x_length04 > 0
                and self.x_length05 > 0 and self.x_length06 > 0 and self.x_length07 > 0
                and self.x_length08 > 0 and self.x_length09 > 0 and self.x_length10 > 0
                and self.x_length11 > 0):
                    record['x_check_complete']=True
                    self.write({'x_check_complete_stored': True})
                    record['x_check_complete_stored']=True
                elif (self.x_qty_inspection_stored == 12 and self.measure > 0
                and self.x_length02 > 0 and self.x_length03 > 0 and self.x_length04 > 0
                and self.x_length05 > 0 and self.x_length06 > 0 and self.x_length07 > 0
                and self.x_length08 > 0 and self.x_length09 > 0 and self.x_length10 > 0
                and self.x_length11 > 0 and self.x_length12 > 0):
                    record['x_check_complete']=True
                    self.write({'x_check_complete_stored': True})
                    record['x_check_complete_stored']=True
                elif (self.x_qty_inspection_stored == 13 and self.measure > 0
                and self.x_length02 > 0 and self.x_length03 > 0 and self.x_length04 > 0
                and self.x_length05 > 0 and self.x_length06 > 0 and self.x_length07 > 0
                and self.x_length08 > 0 and self.x_length09 > 0 and self.x_length10 > 0
                and self.x_length11 > 0 and self.x_length12 > 0
                and self.x_length13 > 0):
                    record['x_check_complete']=True
                    self.write({'x_check_complete_stored': True})
                    record['x_check_complete_stored']=True
                elif (self.x_qty_inspection_stored == 14 and self.measure > 0
                and self.x_length02 > 0 and self.x_length03 > 0 and self.x_length04 > 0
                and self.x_length05 > 0 and self.x_length06 > 0 and self.x_length07 > 0
                and self.x_length08 > 0 and self.x_length09 > 0 and self.x_length10 > 0
                and self.x_length11 > 0 and self.x_length12 > 0 and self.x_length13 > 0
                and self.x_length14 > 0):
                    record['x_check_complete']=True
                    self.write({'x_check_complete_stored': True})
                    record['x_check_complete_stored']=True
                elif (self.x_qty_inspection_stored == 15 and self.measure > 0
                and self.x_length02 > 0 and self.x_length03 > 0 and self.x_length04 > 0
                and self.x_length05 > 0 and self.x_length06 > 0 and self.x_length07 > 0
                and self.x_length08 > 0 and self.x_length09 > 0 and self.x_length10 > 0
                and self.x_length11 > 0 and self.x_length12 > 0 and self.x_length13 > 0
                and self.x_length14 > 0 and self.x_length15 > 0):
                    record['x_check_complete']=True
                    self.write({'x_check_complete_stored': True})
                    record['x_check_complete_stored']=True
                elif (self.x_qty_inspection_stored == 16 and self.measure > 0
                and self.x_length02 > 0 and self.x_length03 > 0 and self.x_length04 > 0
                and self.x_length05 > 0 and self.x_length06 > 0 and self.x_length07 > 0
                and self.x_length08 > 0 and self.x_length09 > 0 and self.x_length10 > 0
                and self.x_length11 > 0 and self.x_length12 > 0 and self.x_length13 > 0
                and self.x_length14 > 0 and self.x_length15 > 0
                and self.x_length16 > 0):
                    record['x_check_complete']=True
                    self.write({'x_check_complete_stored': True})
                    record['x_check_complete_stored']=True
                elif (self.x_qty_inspection_stored == 17 and self.measure > 0
                and self.x_length02 > 0 and self.x_length03 > 0 and self.x_length04 > 0
                and self.x_length05 > 0 and self.x_length06 > 0 and self.x_length07 > 0
                and self.x_length08 > 0 and self.x_length09 > 0 and self.x_length10 > 0
                and self.x_length11 > 0 and self.x_length12 > 0 and self.x_length13 > 0
                and self.x_length14 > 0 and self.x_length15 > 0 and self.x_length16 > 0
                and self.x_length17 > 0):
                    record['x_check_complete']=True
                    self.write({'x_check_complete_stored': True})
                    record['x_check_complete_stored']=True
                elif (self.x_qty_inspection_stored == 18 and self.measure > 0
                and self.x_length02 > 0 and self.x_length03 > 0 and self.x_length04 > 0
                and self.x_length05 > 0 and self.x_length06 > 0 and self.x_length07 > 0
                and self.x_length08 > 0 and self.x_length09 > 0 and self.x_length10 > 0
                and self.x_length11 > 0 and self.x_length12 > 0 and self.x_length13 > 0
                and self.x_length14 > 0 and self.x_length15 > 0 and self.x_length16 > 0
                and self.x_length17 > 0 and self.x_length18 > 0):
                    record['x_check_complete']=True
                    self.write({'x_check_complete_stored': True})
                    record['x_check_complete_stored']=True
                elif (self.x_qty_inspection_stored == 19 and self.measure > 0
                and self.x_length02 > 0 and self.x_length03 > 0 and self.x_length04 > 0
                and self.x_length05 > 0 and self.x_length06 > 0 and self.x_length07 > 0
                and self.x_length08 > 0 and self.x_length09 > 0 and self.x_length10 > 0
                and self.x_length11 > 0 and self.x_length12 > 0 and self.x_length13 > 0
                and self.x_length14 > 0 and self.x_length15 > 0 and self.x_length16 > 0
                and self.x_length17 > 0 and self.x_length18 > 0
                and self.x_length19 > 0):
                    record['x_check_complete']=True
                    self.write({'x_check_complete_stored': True})
                    record['x_check_complete_stored']=True
                elif (self.x_qty_inspection_stored == 20 and self.measure > 0
                and self.x_length02 > 0 and self.x_length03 > 0 and self.x_length04 > 0
                and self.x_length05 > 0 and self.x_length06 > 0 and self.x_length07 > 0
                and self.x_length08 > 0 and self.x_length09 > 0 and self.x_length10 > 0
                and self.x_length11 > 0 and self.x_length12 > 0 and self.x_length13 > 0
                and self.x_length14 > 0 and self.x_length15 > 0 and self.x_length16 > 0
                and self.x_length17 > 0 and self.x_length18 > 0 and self.x_length19 > 0
                and self.x_length20 > 0):
                    record['x_check_complete']=True
                    self.write({'x_check_complete_stored': True})
                    record['x_check_complete_stored']=True
                else:
                    record['x_check_complete']=False
                    self.write({'x_check_complete_stored': False})
                    record['x_check_complete_stored']=False
            else:
                record['x_check_complete']=False
                self.write({'x_check_complete_stored': False})
                record['x_check_complete_stored']=False
