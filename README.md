# generate-doc-sublime-text-plugin-
A sublime text3 plugin for conveniently generate doc

Automatically generate the "@brief,@param " and so on.Modify your shortcuts in the configure file.Note,only support C# now!
Here are some samples:


    /** @interface ICameraEventHandler 
     * @brief 
     */
    public interface ICameraEventHandler
    {}
    
     /** @class MotionController 
     * @brief 
     */
    public class MotionController
    {}
    
     /** @enum IMG_TYPE 
     * @brief 
     */
    public enum IMG_TYPE
    {
        JPEG=1,
        PNG,
        TIFF,
        BMP
    }
    
    /** @struct  
     * @brief 
    */
    public  struct  Picture
    {}
    
   
    public string ProjectSavePath = "C:\\";///<
    
   
    /** @brief 
    * @param t1 
    * @param t2 
    */
     public override void Save(int t1,double t2   = 1) //multi blank in parameter t2
   
    /** @brief 
     * @param x 
     * @param y 
     * @param z 
    */
     public override void Move(float x, float y,float z)//parameters cross multi-line 
     {}
   
    
    
