# -*- coding: utf-8 -*-

listaa = ['uid','paperId','states','operatorCompany','recordRoomId','title','teacherName','signature','liveRoomSignature','liveId','endTime','startTime','subscribeNum','ccPlaybackId','ccliveId','startDate','hasQuizz','livePicUrl','authorityUserId']


for str in listaa :
    print '-(NSString *)',str,'{\n    if([_',str,' isKindOfClass:[NSNull class]]){\n        return nil;\n    }\n    return _',str,';\n}\n'
    pass