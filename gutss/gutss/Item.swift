//
//  Item.swift
//  gutss
//
//  Created by Cobb, Morgan L. on 1/19/24.
//

import Foundation
import SwiftData

@Model
final class Item {
    var timestamp: Date
    
    init(timestamp: Date) {
        self.timestamp = timestamp
    }
}
