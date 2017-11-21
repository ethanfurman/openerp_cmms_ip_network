# -*- coding: utf-8 -*-
################################################################################
#
# CMMS link to IP Map module,
#
################################################################################


from osv import fields, osv
import logging

_logger = logging.getLogger(__name__)


# Equipment
#
class equipment_ip(osv.Model):
    'equipment w/IP address'
    _name = 'cmms.equipment'
    _inherit = 'cmms.equipment'
    _description = 'equipment'
    _order = 'name asc'

    _columns = {
        'ip_addr_id': fields.many2one('ip_map.device', 'IP address'),
        }

    def copy(self, cr, uid, id, default=None, context=None):
        if default is None:
            default = {}
        default = default.copy()
        default['ip_addr_id'] = False
        return super(equipment_ip, self).copy(cr, uid, id, default=default, context=context)

