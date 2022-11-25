from odoo import http
from odoo.http import request
import base64

class FoodPage(http.Controller):
		
	@http.route(route='/home',type='http',auth='public',website=True)
	def home_page(self,**kw):
		# customers = request.env['res.partner'].search([])
		return request.render('revision_tasks.food_templates',{})