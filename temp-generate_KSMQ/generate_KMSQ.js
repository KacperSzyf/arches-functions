define(['jquery',
    'knockout',
    'viewmodels/function',
    'bindings/chosen', 'arches'],
function($, ko, FunctionViewModel, chosen, arches) {
    return ko.components.register('views/components/functions/generate_KMSQ', {
        viewModel: function(params) {
            FunctionViewModel.apply(this, arguments);
            let self = this
            //Params ---
            this.triggering_nodegroups = params.config.triggering_nodegroups;
            //end params
            this.triggering_nodegroups(['5844718c-7dcc-11ec-a910-00155db3508e'])
        }//5844718c-7dcc-11ec-a910-00155db3508e
        ,
        template: {
            require: 'text!templates/views/components/functions/generate_KMSQ.htm'

        }
    });
});
