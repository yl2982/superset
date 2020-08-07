import {t} from '@superset-ui/translation';
import {ChartMetadata, ChartPlugin} from '@superset-ui/chart';
import transformProps from './transformProps';
import controlPanel from './controlPanel';
import thumbnail from './images/thumbnail.png';

const metadata = new ChartMetadata({
    name: t('EChart Funnel'),
    description: '',
    thumbnail,
});

export default class FunnelPlugin extends ChartPlugin {
    constructor() {
        super({
            metadata,
            transformProps,
            controlPanel,
            loadChart: () => import('./Funnel.jsx'),
        });
    }
}
