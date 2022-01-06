for i in range (0,11):
    print("part_textview[%d] = new Part_textview();"%(i,))
    print("part_textview[%d].part_p1 = view.findViewById(R.id.fi_xml_part%d_p1);"%(i,i+1))
    print("part_textview[%d].part_score = view.findViewById(R.id.fi_xml_part%d_score);"%(i,i+1))
    print("part_textview[%d].part_p2 = view.findViewById(R.id.fi_xml_part%d_p2);"%(i,i+1))
    print("parntership[%d] = view.findViewById(R.id.fi_xml_part%d);"%(i,i+1))
    print("\n")
    
