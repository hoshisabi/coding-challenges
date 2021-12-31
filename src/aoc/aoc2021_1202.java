package aoc;

import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.*;
import java.util.stream.Collectors;

public class aoc2021_1202
{
  public static class Node
  {
    String name;
    List<Node> neighbors;
    boolean large = false;

    public Node(String name)
    {
      this.name = name;
      neighbors = new ArrayList<>();

      if (name.toUpperCase().equals(name))
      {
        large = true;
      }
    }

    public void addNeighbor(Node neighbor)
    {
      if (!neighbors.contains(neighbor))
      {
        neighbors.add(neighbor);
      }
    }

    public String getName()
    {
      return name;
    }

    public boolean isLarge()
    {
      return large;
    }

    public List<Node> getNeighbors()
    {
      return neighbors;
    }
  }

  public static class NodeMap
  {
    Map<String, Node> nodeMap;

    public NodeMap()
    {
      nodeMap = new HashMap<>();
    }

    public void addConnection(String route)
    {
      String[] nodeString = route.split("-");

      String leftString = nodeString[0];
      String rightString = nodeString[1];
      Node leftNode = nodeMap.get(leftString);
      Node rightNode = nodeMap.get(rightString);

      if (leftNode == null)
      {
        leftNode = new Node(leftString);
        nodeMap.put(leftString, leftNode);
      }

      if (rightNode == null)
      {
        rightNode = new Node(rightString);
        nodeMap.put(rightString, rightNode);
      }

      leftNode.addNeighbor(rightNode);
      rightNode.addNeighbor(leftNode);
    }

    public Node getStartNode()
    {
      return nodeMap.get("start");
    }

    public Node getEndNode()
    {
      return nodeMap.get("end");
    }

    @Override
    public String toString()
    {
      return "NodeMap{" +
          "nodeMap=" + nodeMap +
          '}';
    }
  }

  public class NodePath
  {
    List<Node> nodePath;
    boolean visitedSmallTwice = false;

    public NodePath(NodePath path)
    {
      nodePath = new ArrayList<>(path.getNodePath());
      visitedSmallTwice = path.isVisitedSmallTwice();
    }

    public NodePath(Node startNode)
    {
      nodePath = new ArrayList<>(Collections.singletonList(startNode));
    }

    public void addNode(Node newNode)
    {
      if (!newNode.isLarge() && nodePath.contains(newNode))
      {
        visitedSmallTwice = true;
      }
      nodePath.add(newNode);
    }

    public boolean legalAddition(Node newNode)
    {
      if (newNode.getName().equals("start"))
      {
        return false;
      }

      if (newNode.isLarge())
      {
        return true;
      }

      return !visitedSmallTwice || !nodePath.contains(newNode);
    }

    public Node getLastNode()
    {
      return nodePath.get(nodePath.size() - 1);
    }

    public List<Node> getNodePath()
    {
      return nodePath;
    }

    public boolean isVisitedSmallTwice()
    {
      return visitedSmallTwice;
    }


    public String getPathString()
    {
      return nodePath.stream().map(Node::getName).collect(Collectors.joining(","));
    }
  }

  public aoc2021_1202(String filename) throws IOException, URISyntaxException
  {
    URI uri = this.getClass().getResource(filename).toURI();
    List<String> lines = Files.readAllLines(Paths.get(uri), Charset.defaultCharset());
    NodeMap nodeMap = new NodeMap();
    for (String line : lines)
    {
      nodeMap.addConnection(line);
    }

    System.out.println("nodeMap = " + nodeMap);

    List<NodePath> partialPaths = new ArrayList<>();
    NodePath startPath = new NodePath(nodeMap.getStartNode());
    partialPaths.add(startPath);

    List<NodePath> endingPaths = new ArrayList<>();

    while (!partialPaths.isEmpty())
    {
      List<NodePath> newPaths = new ArrayList<>();
      for (NodePath path : partialPaths)
      {
        Node lastRoom = path.getLastNode();
        List<Node> neighbors = lastRoom.getNeighbors();
        for (Node neighbor : neighbors)
        {
          if (path.legalAddition(neighbor))
          {
            NodePath newPath = new NodePath(path);
            newPath.addNode(neighbor);

            if (neighbor == nodeMap.getEndNode())
            {
              endingPaths.add(newPath);
            }
            else
            {
              newPaths.add(newPath);
            }
          }
        }
      }
      partialPaths = newPaths;
    }
    System.out.println(endingPaths.stream().map(NodePath::getPathString).collect(Collectors.joining("\n")));
    System.out.println("number of paths = " + endingPaths.size());
  }

  public static void main(String[] args)
  {
    try
    {
//      aoc2021_1202 me = new aoc2021_1202("aoc2021_1201_testinput.txt"); // expect 36
//      aoc2021_1202 me = new aoc2021_1202("aoc2021_1201_testinput2.txt"); // expect 103
//      aoc2021_1202 me = new aoc2021_1202("aoc2021_1201_testinput3.txt"); // expect 3509
      aoc2021_1202 me = new aoc2021_1202("aoc2021_1201_input.txt");
    }
    catch (Exception e)
    {
      e.printStackTrace();
    }
  }
}
