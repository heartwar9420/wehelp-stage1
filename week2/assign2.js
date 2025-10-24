function func1(name) {
    // your code here
    function distance(p1, p2) {
        const [x1, y1, z1] = p1;
        const [x2, y2, z2] = p2;
        let dist = Math.abs(x1 - x2) + Math.abs(y1 - y2);
        if (z1 !== z2) {
            dist += 2;
        }
        return dist;
    }

    const 悟空 = [0, 0, 0]; // (X,Y,Z)
    const 特南克斯 = [1, -2, 0];
    const 辛巴 = [-3, 3, 0];
    const 貝吉塔 = [-4, -1, 0];
    const 丁滿 = [-1, 4, 1];
    const 弗利沙 = [4, -1, 1];

    const points = {
        "悟空": 悟空,
        "特南克斯": 特南克斯,
        "辛巴": 辛巴,
        "貝吉塔": 貝吉塔,
        "丁滿": 丁滿,
        "弗利沙": 弗利沙,
    };

    const target = points[name];
    const results = [];

    for (const [other_name, other_pt] of Object.entries(points)) {
        if (other_name === name) continue;
        const d = distance(target, other_pt);
        results.push([other_name, d]);
    }

    results.sort((a, b) => a[1] - b[1]);

    const min_distance = results[0][1];
    const max_distance = results[results.length - 1][1];

    const nearest = [];
    for (const [n, d] of results) {
        if (d === min_distance) {
            nearest.push(n);
        }
    }

    const farthest = [];
    for (const [n, d] of results) {
        if (d === max_distance) {
            farthest.push(n);
        }
    }

    console.log(
        "最遠的是：",
        farthest.join("、"),
        "；最近的是：",
        nearest.join("、")
    );
}

console.log("=== Task 1 ===");
func1("辛巴");     // print 最遠弗利沙；最近丁滿、貝吉塔
func1("悟空");     // print 最遠丁滿、弗利沙；最近特南克斯
func1("弗利沙");   // print 最遠辛巴；最近特南克斯
func1("特南克斯"); // print 最遠丁滿；最近悟空

// your code here, maybe
function func2(ss, start, end, criteria) {
    // your code here
    if (!func2.bookings) {
        func2.bookings = {};
        for (const s of ss) {
            func2.bookings[s.name] = [];
        }
    }

    let field = " ";
    let op = " ";
    let raw_value = " ";

    if (criteria.includes(">=")) {
        [field, raw_value] = criteria.split(">=");
        op = ">=";
    } else if (criteria.includes("<=")) {
        [field, raw_value] = criteria.split("<=");
        op = "<=";
    } else if (criteria.includes("=")) {
        [field, raw_value] = criteria.split("=");
        op = "=";
    } else {
        console.log("Sorry");
        return;
    }

    field = field.trim();
    raw_value = raw_value.trim();

    function is_available(ss_name) {
        const bookedList = func2.bookings[ss_name] || [];
        for (const [a, b] of bookedList) {
            if (!(end <= a || start >= b)) {
                return false;
            }
        }
        return true;
    }

    let candidates = [];

    if (field === "name") {
        for (const s of ss) {
            if (s.name === raw_value && is_available(s.name)) {
                candidates.push(s);
            }
        }
    } else {
        const val = parseFloat(raw_value);

        for (const s of ss) {
            const fv = parseFloat(s[field]);
            const ok =
                (op === ">=" && fv >= val) ||
                (op === "<=" && fv <= val);
            if (ok && is_available(s.name)) {
                candidates.push(s);
            }
        }
    }

    if (op === ">=") {
        candidates.sort((a, b) => {
            if (a[field] === b[field]) {
                return a.name.localeCompare(b.name);
            }
            return a[field] - b[field];
        });
    } else {
        candidates.sort((a, b) => {
            if (a[field] === b[field]) {
                return a.name.localeCompare(b.name);
            }

            return b[field] - a[field];
        });
    }

    if (candidates.length > 0) {
        const chosen = candidates[0];
        if (!func2.bookings[chosen.name]) {
            func2.bookings[chosen.name] = [];
        }
        func2.bookings[chosen.name].push([start, end]);
        console.log(chosen.name);
    } else {
        console.log("Sorry");
    }
}

const services = [
    { name: "S1", r: 4.5, c: 1000 },
    { name: "S2", r: 3, c: 1200 },
    { name: "S3", r: 3.8, c: 800 },
];
console.log("=== Task 2 ===");
func2(services, 15, 17, "c>=800");   // S3
func2(services, 11, 13, "r<=4");     // S3
func2(services, 10, 12, "name=S3");  // Sorry
func2(services, 15, 18, "r>=4.5");   // S1
func2(services, 16, 18, "r>=4");     // Sorry
func2(services, 13, 17, "name=S1");  // Sorry
func2(services, 8, 9, "c<=1500");    // S2


function func3(index) {
    // your code here
    let num = 23;
    const sequence = [-2, -3, 1, 2];

    for (let i = 0; i < index - 1; i++) {
        const result = sequence[(i + 1) % sequence.length];
        num = num + result;
    }
    console.log(num);
}

console.log("=== Task 3 ===");
func3(1);   // 23
func3(5);   // 21
func3(10);  // 16
func3(30);  // 6


function func4(sp, stat, n) {
    const usable = [];
    for (let i = 0; i < sp.length; i++) {
        if (stat[i] === '0') {
            usable.push(i);
        }
    }

    const enough = [];
    for (const i of usable) {
        if (sp[i] >= n) {
            enough.push(i);
        }
    }

    if (enough.length > 0) {
        let min_i = enough[0];
        for (const i of enough) {
            if (sp[i] < sp[min_i]) {
                min_i = i;
            }
        }
        console.log(min_i);
    } else {
        const less = [];
        for (const i of usable) {
            if (sp[i] < n) {
                less.push(i);
            }
        }

        let max_i = less[0];
        for (const i of less) {
            if (sp[i] > sp[max_i]) {
                max_i = i;
            }
        }
        console.log(max_i);
    }
}

console.log("=== Task 4 ===");
func4([3, 1, 5, 4, 3, 2], "101000", 2); // 5
func4([1, 0, 5, 1, 3],     "10100",  4); // 4
func4([4, 6, 5, 8],        "1000",   4); // 2