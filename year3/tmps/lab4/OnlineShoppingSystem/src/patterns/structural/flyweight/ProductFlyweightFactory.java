package patterns.structural.flyweight;

import java.util.HashMap;
import java.util.Map;

// Factory to create and manage Flyweight objects
public class ProductFlyweightFactory {
    private static final Map<String, ProductFlyweight> flyweights = new HashMap<>();

    public static ProductFlyweight getProductTypeData(String category, double discountRate, String brand) {
        String key = category + "-" + discountRate + "-" + brand;
        if (!flyweights.containsKey(key)) {
            flyweights.put(key, new ProductTypeData(category, discountRate, brand));
        }
        return flyweights.get(key);
    }
}

