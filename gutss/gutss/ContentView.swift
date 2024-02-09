//
//  ContentView.swift
//  gutss
//
//  Created by Cobb, Morgan L. on 1/19/24.
//  hello world

import SwiftUI
import SwiftData

struct ContentView: View {
    @Environment(\.modelContext) private var modelContext
    @Query private var items: [Item]

    var body: some View {
        ZStack {
            Image("UFBlue")
                .resizable().ignoresSafeArea()
            
            VStack {
                
                Spacer()
                VStack{
                    
                    Text("GUTSS").font(.title)
                        .fontWeight(/*@START_MENU_TOKEN@*/.bold/*@END_MENU_TOKEN@*/)
                        .foregroundColor(Color.black)
                        .padding()
                    Text("Welcome to Guided Undergraduate Training for Shark Segmentation")
                        .multilineTextAlignment(.center)
                        .foregroundColor(Color.black)
                        .padding()
                    Button("Get Started") {
                        /*@START_MENU_TOKEN@*//*@PLACEHOLDER=Action@*/ /*@END_MENU_TOKEN@*/
                    }
                }
                .padding()
                .background(Rectangle().foregroundColor(.white).cornerRadius(15.0)).padding()
                
                Spacer()
                Text("Powered by:")
                    .foregroundColor(Color.white)
                Image("square-logo")
                    .resizable()
                    .aspectRatio(contentMode: .fit)
                    .frame(width: 100.0)
            }
        }
        
    }
}

   
#Preview {
    ContentView()
        .modelContainer(for: Item.self, inMemory: true)
}
