using UnityEngine;
using Unity.MLAgents;
using Unity.MLAgents.Actuators;
using Unity.MLAgents.Sensors;

public class FallingStarAgent : Agent
{
    public GameObject wall1;
    public GameObject wall2;
    public GameObject env;

    private float distance1;
    private float distance2;

    public override void Initialize()
    {
        distance1 = (this.transform.position - wall1.transform.position).magnitude;
        distance2 = (this.transform.position - wall2.transform.position).magnitude;
    }

    public override void CollectObservations(VectorSensor sensor)
    {
        distance1 = (this.transform.position - wall1.transform.position).magnitude;
        distance2 = (this.transform.position - wall2.transform.position).magnitude;
        sensor.AddObservation(distance1);
        sensor.AddObservation(distance2);
    }

    public override void OnActionReceived(ActionBuffers actionBuffers)
    {
        var act0 = actionBuffers.DiscreteActions[0];
        var reward = 0f;
        switch (act0)
        {
            case 1:
                this.transform.position += new Vector3(-0.2f, 0f, 0f);
                //Debug.Log("Get1");
                break;

            case 2:
                this.transform.position += new Vector3(0.2f, 0f, 0f);
                //Debug.Log("Get2");
                break;

            default:
                this.transform.position += new Vector3(0f, 0f, 0f);
                break;
        }

        distance1 = (this.transform.position - wall1.transform.position).magnitude;
        distance2 = (this.transform.position - wall2.transform.position).magnitude;
        reward = Random.Range(-1f, 1f);
        AddReward(reward);
    }

    public override void OnEpisodeBegin()
    {
        this.transform.position = env.transform.position;
    }


    public override void Heuristic(in ActionBuffers actionsOut)
    {
        var DiscreteActionsout = actionsOut.DiscreteActions;
        DiscreteActionsout[0] = 0;
        if (Input.GetKey(KeyCode.A))
        {
            DiscreteActionsout[0] = 1;
        }
        if (Input.GetKey(KeyCode.D))
        {
            DiscreteActionsout[0] = 2;
        }
    }
}
