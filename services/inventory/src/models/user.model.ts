import {Entity, model, property, hasMany} from '@loopback/repository';
import { Product } from './product.model';

@model()
export class User extends Entity {
  @property({
    type: 'number',
    id: true,
    generated: true,
  })
  id?: number;

  @property({
    type: 'string',
    required: true,
  })
  username: string;

  @hasMany(() => Product)
  products: Product[];

  constructor(data?: Partial<User>) {
    super(data);
  }
}

export interface UserRelations {
  // describe navigational properties here
  products?: Product[];
}

export type UserWithRelations = User & UserRelations;
