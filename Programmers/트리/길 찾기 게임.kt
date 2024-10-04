data class Node(
    val idx: Int,
    val x: Int,
    val y: Int,
    var left: Node? = null,
    var right: Node? = null
)

class Solution {
    private val preorderList = mutableListOf<Int>()
    private val postorderList = mutableListOf<Int>()

    private fun insertNode(parent: Node, child: Node) {
        if (child.x < parent.x) {
            if (parent.left == null) {
                parent.left = child
            } else {
                insertNode(parent.left!!, child)
            }
        } else {
            if (parent.right == null) {
                parent.right = child
            } else {
                insertNode(parent.right!!, child)
            }
        }
    }

    private fun preorder(node: Node?) {
        if (node == null) return
        preorderList.add(node.idx)
        preorder(node.left)
        preorder(node.right)
    }

    private fun postorder(node: Node?) {
        if (node == null) return
        postorder(node.left)
        postorder(node.right)
        postorderList.add(node.idx)
    }

    fun solution(nodeinfo: Array<IntArray>): Array<IntArray> {
        val nodes = nodeinfo.mapIndexed { idx, info -> 
            Node(idx + 1, info[0], info[1])
        }

        val sortedNodes = nodes.sortedWith(compareBy({ -it.y }, { it.x }))
        val root = sortedNodes[0]

        for (i in 1 until sortedNodes.size) {
            insertNode(root, sortedNodes[i])
        }

        preorder(root)
        postorder(root)

        return arrayOf(preorderList.toIntArray(), postorderList.toIntArray())
    }
}