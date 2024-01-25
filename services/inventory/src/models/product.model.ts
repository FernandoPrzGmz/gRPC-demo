import {Entity, model, property, hasOne, belongsTo} from '@loopback/repository';
import { v4 as uuidv4 } from 'uuid';

import { Inventory } from './inventory.model';
import { User } from './user.model';

@model()
export class Product extends Entity {
  @property({
    type: 'string',
    id: true,
    default: () => uuidv4(),
  })
  id: string;

  @property({
    type: 'string',
    required: true,
  })
  name: string;

  @property({
    type: 'number',
    required: true,
  })
  price: number;

  @property({
    type: 'string',
  })
  description?: string;

  @property({
    type: 'object',
  })
  dimensions?: object;

  @hasOne(() => Inventory)
  inventory: Inventory;

  @belongsTo(() => User)
  userId: number; // Referencia al usuario que dio de alta el producto

  constructor(data?: Partial<Product>) {
    super(data);
  }
}

export interface ProductRelations {
  // describe navigational properties here
  inventory?: Inventory;
  user?: User;
}

export type ProductWithRelations = Product & ProductRelations;
