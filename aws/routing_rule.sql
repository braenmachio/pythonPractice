select 
    state.reported.ts as dataTimestamp,
    topic(1) as deviceId,
    state.reported.latlng as coordinates,
    state.reported.239 as ignitionStatus,
    state.reported.240 as movementStatus
from '352592573813961/data'