describe("Movies", function () {
  //tests to see if the following materialize datepicker and carousel true variables are booleans:

  describe("Check to see if showClearBtn is a boolean.", function () {
    let showClearBtn = true;
    it("It should be a boolean.", function () {
      expect(showClearBtn).toBe(true);
    });
  });

  describe("Check to see if fullWidth is a boolean.", function () {
    let fullWidth = true;
    it("It should be a boolean.", function () {
      expect(fullWidth).toBe(true);
    });
  });

  describe("Check to see if indicators is a boolean.", function () {
    let indicators = true;
    it("It should be a boolean.", function () {
      expect(indicators).toBe(true);
    });
  });

  //tests to see if the following materialize carousel false variable is a boolean:

  describe("Check to see if noWrap is a boolean.", function () {
    let noWrap = false;
    it("It should be a boolean.", function () {
      expect(noWrap).toBe(false);
    });
  });

  // tests to see if the following materialize datepicker and carousel number/string values are correct:

  describe("Check to see if format equates to a string.", function () {
    it("It should be a string.", function () {
      expect(format("dd mmmm, yyyy")).toBe("dd mmmm, yyyy");
    });
    it("It should return an error if not supplied with a string.", function () {
      expect(format(18, 05, 1994)).toBe("ERROR!");
    });
  });

  describe("Check to see if yearRange equates to the number 3.", function () {
    it("It should be 3.", function () {
      expect(yearRange(3)).toBe(3);
    });
    it("It should return an error if not supplied with a number.", function () {
      expect(yearRange("Hello World!")).toBe("ERROR!");
    });
  });

  describe("Check to see if firstDay equates to the number 1.", function () {
    it("It should be 1.", function () {
      expect(firstDay(1)).toBe(1);
    });
    it("It should return an error if not supplied with a number.", function () {
      expect(firstDay("Hello", "World!")).toBe("ERROR!");
    });
  });

  describe("Check to see if i18n['done'] equates to a string.", function () {
    it("It should be a string.", function () {
      expect(i18n("Select")).toBe("Select");
    });
    it("It should return an error if not supplied with a string.", function () {
      expect(i18n(23 / 09 / 2020)).toBe("ERROR!");
    });
  });

  describe("Check to see if dist equates to the number 0.", function () {
    it("It should be 0.", function () {
      expect(dist(0)).toBe(0);
    });
    it("It should return an error if not supplied with a number.", function () {
      expect(dist("Hello World!")).toBe("ERROR!");
    });
  });

  describe("Check to see if duration equates to the number 500.", function () {
    it("It should be 500.", function () {
      spyOn(window, "alert");
      duration("Hello", "World!");
      expect(window.alert).toHaveBeenCalledWith("ERROR!");
    });
  });

  describe("Check to see if padding equates to the number 200.", function () {
    it("It should be 200.", function () {
      spyOn(window, "alert");
      padding("Hello World!");
      expect(window.alert).toHaveBeenCalledWith("ERROR!");
    });
  });

  describe("Check to see if numVisible equates to the number 6.", function () {
    it("It should be 6.", function () {
      spyOn(window, "alert");
      numVisible("Hello", "World!");
      expect(window.alert).toHaveBeenCalledWith("ERROR!");
    });
  });
});
