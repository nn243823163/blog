
/**
 * Created by doudou on 16/8/28.
 */

KindEditor.ready(function(K) {
    // 配置富文本编辑器
    K.create('textarea[name=content]',{
        width:'1000px',
        height:'200px',
        uploadJson: '/admin/upload/kindeditor',

    });

});
