import {Entity, model, property, belongsTo} from '@loopback/repository';
import { Product } from './product.model';

@model()
export class Inventory extends Entity {
  @property({
    type: 'number',
    id: true,
    generated: true,
  })
  id?: number;

  @property({
    type: 'number',
    required: true,
  })
  quantity: number;

  @belongsTo(() => Product)
  productId: number;


  constructor(data?: Partial<Inventory>) {
    super(data);
  }
}

export interface InventoryRelations {
  // describe navigational properties here
  product?: Product;
}

export type InventoryWithRelations = Inventory & InventoryRelations;
