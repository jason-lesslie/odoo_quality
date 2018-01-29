# Quality Check Model
The purpose of this quality check model is to prompt the user to enter a specified number of measurements for five parameters. In this case the five parameters are length, perpendicularity, height, number of pleats, and width. The specified number of measurements is calculated as 10% of production quantity. Only the required fields for the user to fill out are displayed. The Validate button becomes visible when all required fields have a value greater than zero. This prevents the user from forgetting to fill in a measurement field. This customization was needed because Odoo out of the box was only capable of entering one measurement regardless of the production quantity.

To avoid interference with existing field names all custom field names begin with `x_`

`@api.depends()` are the dependencies used to calculate that particular field

`def x_min_measured_length(self):` defines the function and takes in the self object, which in this case is `MrpQualityCheck` object model.

`for record in self:` loops through the self object to assign a value for a given key. In this case the key is the calculated field name such as `x_min_measured_length`

### Minimum Function Workaround
In Odoo null fields are not allowed and they have a default value of 0. So the `min()` function needed to be adjusted to ignore the fields with a value of 0.

Inside the `min()` function I used an anonymous function that returns a tuple (True/False, x). When the `x_length02` field's value is 0 the lambda functions returns (True, x). When the `x_length02` field's value is not 0 the lambda functions returns (False, x). For case when field is not 0 the lambda functions returns (False, x). The `min()` will first sort based on the True/False value then sort based on the value of `x`. Since True has a value of 1 and False has a value of 0, this results in the `min()` function returning the smallest non-zero length.

### Inspection Fail Function
The fail function contains an if statement to first check that the minimum length `x_min_measured_length` is greater that zero, which occurs when the user enters the first length value. This prevents **FAIL** from displaying before the user has entered any measurements. The nested if statement checks if the min length is less than the min tolerance *or* if the max length is greater than the max tolerance. If either of these statements is true, the "FAIL" string will be assigned to the `x_length_fail` field.

### Inspection Quantity
The quantity of measurements the user is required to enter is calculated automatically with the `x_qty_inspection` field. Different work center stations have different maximum measurements caps. For example the code below sets a cap of 10 inspections for work center ID number 5.
```python
@api.depends('x_qty_production','workcenter_id')
  def x_qty_inspection(self):
      for record in self:
          if self.x_qty_production*.1 >= 10 and self.workcenter_id.id == 5:
              record['x_qty_inspection']=10
              self.write({'x_qty_inspection_stored': 10})
              record['x_qty_inspection_stored']=10
```
To handle the case when 10% of the production quantity is less than or equal to 1 the inspection quantity was set to zero as shown in the code section below.
```python
def x_qty_inspection(self):
    for record in self:
      # code
        elif self.x_qty_production*.1 <= 1 and self.workcenter_id.id != 1:
            record['x_qty_inspection']=1
            self.write({'x_qty_inspection_stored': 1})
            record['x_qty_inspection_stored']=1
```
To handle the case when 10% of the production quantity is less than the max inspection quantity and greater than 1 the `round()` function was used to round the float number to the closest integer.
```python
def x_qty_inspection(self):
    for record in self:
        # code
        elif self.workcenter_id.id != 1:
            record['x_qty_inspection']=round(self.x_qty_production*.1)
            self.write({'x_qty_inspection_stored': round(self.x_qty_production*.1)})
            record['x_qty_inspection_stored']=round(self.x_qty_production*.1)
```

### Check Complete
The `x_check_complete` field is a boolean field that returns a value of `True` when all required measurements have been entered. This field is used to set the Validate button to visible to allow the user to save the measurements and proceed to the next work center.

To handle work centers with different required fields a series of `elif` statements was used as seen in the code below.
```python
def x_check_complete(self):
    for record in self:
        if (self.x_seal_in_place == True and self.x_passed_visual_inspection == True
        and self.workcenter_id.id == 5):
          # nested if statements
        elif self.workcenter_id.id == 1 and self.x_product_material == 'metal':
          # nested if statements
        elif self.workcenter_id.id == 1 and self.x_product_material == 'nylon':
          # nested if statements
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
```
For the case with work center id 2 with a quantity inspection equal to 2 the fields `measure` and `x_length02` fields need to be greater than 0. The `x_check_complete_stored` field is only set to `True` when all of these conditions are satisfied.

### Quality Check View XML File
The custom fields were added to view. All inspection fields that do not require user input are hidden from the user using the `invisible` property. All field dependencies of calculated fields must be included in the XML file for the calculated field to properly function. Non-helpful fields such as the `x_min_height` field are set to invisible to reduce clutter of the view.

### Process Flowchart
See the QualityFlowchart.png file for detail on how this application functions.

### Youtube Video
In this video I show two examples. The first example has a production quantity of 20 and the second example has a production quantity of 95. The application is setup to require 10% inspection. So the first example should have prompt the user for 2 measurements and the second example should prompt the user for 10 measurements. `round(.10 * 95) = round(9.5) = 10`

<https://www.youtube.com/watch?v=QNegABwC56U>
