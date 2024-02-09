//
//  myModel.swift
//  gutss
//
//  Created by Wu, Amy on 2/9/24.
//

import Foundation
import CoreML

guard let model = try? VNCoreMLModel(for: myModel().model) else {
    fatalError("Failed to load Core ML model")
}
