using System.Collections;
using System.Collections.Generic;
using UnityEngine;

/*
    - one method could be that we could use an n x n x n grid composed of (transparent?) cubes which would then
        light up based on a binary value 1 and off when 0. 
        - We can then easily work off of this and impliment what cubes should light up.
        - add an editor where you can create your own initial state 
        - maybe? : add a randomizer where you can create initial states randomly 



        TODO: 
            - optimize cube rendering

                approaches:
                    - occlusion culling:
                        -https://stackoverflow.com/questions/25612187/c-sharp-unity-3d-1000-cube-instantiation-scriptS
                    - entity component system:
                        - https://learn.unity.com/tutorial/entity-component-system#5c7f8528edbc2a002053b678
                        - https://answers.unity.com/questions/1756928/drawing-100-000-cubes.html
                        - https://levelup.gitconnected.com/a-simple-guide-to-get-started-with-unity-ecs-b0e6a036e707

                    
                    - Add a way to remove a gameObject from scene in order to create new state
*/

public class VoxelCube : MonoBehaviour
{
    public List<Vector3> locations = new List<Vector3>();
    public List<Vector3> adjacentCubes = new List<Vector3>();

    public Dictionary<Vector3, bool> onOff = new Dictionary<Vector3, bool>(); 
    public bool swatch = true;
    private float nextActionTime = 5.0f;
    public float period = 1.0f;
 
    private void initializeRandomState(){
    //initialization
       for(int x=0; x<40; x+=2){
           for(int y=0; y<40; y+=2){
               for(int z=0; z<40; z+=2){
                   locations.Add(new Vector3(x, y, z));
                   int val = Random.Range(0, 10);
                   if(val < 2){
                    onOff.Add(new Vector3(x, y, z), true);
                   }else{
                       onOff.Add(new Vector3(x, y, z), false);
                   }
               }
           }
       }
   }

   private void neighborOn(new Vector3){


       return;
   }

    private void changeState(Dictionary<Vector3, bool> newBoard){
        //uses the rules for a 3-dimensional game of life to update the board and render a new one every frame

       for(int x=0; x<40; x+=2){
           for(int y=0; y<40; y+=2){
               for(int z=0; z<40; z+=2){
                   locations.Add(new Vector3(x, y, z));

                    for(int x=0; x<24; x++){
                        if(neighborOn(new Vector3(x, y, z))){
                            count++;
                        }
                    }

                    if(program==false){
                        newBoard[new Vector3(x, y, z)] = false;
                    }else if(){
                        newBoard[new Vector3(x, y, z)] = true;
                    }else if(){
                        newBoard[new Vector3(x, y, z)] = false;
                    }else if(){
                        newBoard[new Vector3(x, y, z)] = true;
                    }

                    newBoard[new Vector3(x, y, z)] = true;
                    
               }
           }
       }
   }
   
    private void clearScreen(){
       foreach(GameObject o in Object.FindObjectsOfType<GameObject>()){
           if(o.name == "Main Camera" || o.name == "ground" || o.name == "Directional Light"){
               continue;
           }
           Destroy(o);
       }
    }

    private void renderCubes(){
       //rendering the cubes
       //I think its good for creating the initial state
       Debug.Log("is it working?");
       for(int x=0; x<40; x+=2){
           for(int y=0; y<40; y+=2){
               for(int z=0; z<40; z+=2){

                   if(onOff[new Vector3(x, y, z)] == true)
                       VoxelTools.makeCube(x, y, z);
               }
           }
       }
       Debug.Log("yes it is working you dimwit");

    }

    void Start(){
        initializeRandomState();
        renderCubes();
    }

    void Update() {
        /*
        while the game is running
        check to see if rules apply for each cube in the matrix -- I know this is fucking slow but we shall see
            - if the rule is applicable then change state 
            - we have the isse of double counting
                - turning real messy real quick
                - one thing to note is that the simulation has to be parallel?
                    - NO
            - create a brand new board and encode new state into new board so there won't be doubel counting or overlap
        */

        if(Time.time > nextActionTime){
            nextActionTime += period;
            List<Vector3> tempBoard = new List<Vector3>(); 
            Dictionary<Vector3, bool> tempBoardState = onOff;

            Debug.Log("--RENDERING--");

            clearScreen();
//            changeState(tempBoardState);
            renderCubes();

        }
    }
}
