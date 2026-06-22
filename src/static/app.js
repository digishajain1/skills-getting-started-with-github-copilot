document.addEventListener("DOMContentLoaded", () => {
  const resourcesList = document.getElementById("resources-list");
  const scheduleList = document.getElementById("schedule-list");
  const slotSelect = document.getElementById("slot");
  const signupForm = document.getElementById("signup-form");
  const messageDiv = document.getElementById("message");
  const handbookDiv = document.getElementById("handbook");

  function showMessage(text, type) {
    messageDiv.textContent = text;
    messageDiv.className = `message ${type}`;
    messageDiv.classList.remove("hidden");
  }

  function renderTeacherResources(resources) {
    resourcesList.innerHTML = "";

    Object.entries(resources).forEach(([grade, details]) => {
      const resourceCard = document.createElement("article");
      resourceCard.className = "resource-card";
      resourceCard.innerHTML = `
        <h4>${grade}</h4>
        <p>${details.focus}</p>
        <p><strong>Subjects:</strong> ${details.subjects.join(", ")}</p>
        <ul>${details.goals.map((goal) => `<li>${goal}</li>`).join("")}</ul>
      `;
      resourcesList.appendChild(resourceCard);
    });
  }

  function renderSchedule(schedule) {
    scheduleList.innerHTML = "";
    slotSelect.innerHTML = '<option value="">-- Select a class slot --</option>';

    Object.entries(schedule).forEach(([day, slots]) => {
      const dayCard = document.createElement("article");
      dayCard.className = "day-card";
      const weekendLabel = slots.length === 5 ? "Weekend intensive" : "Weekday track";

      dayCard.innerHTML = `<h4>${day}</h4><p class="day-meta">${weekendLabel} · ${slots.length} classes</p>`;

      const slotItems = document.createElement("div");
      slotItems.className = "slot-items";

      slots.forEach((slot) => {
        const isFilled = slot.volunteers.length >= slot.max_volunteers;
        const slotCard = document.createElement("div");
        slotCard.className = `slot-card${isFilled ? " slot-card-filled" : ""}`;
        slotCard.innerHTML = `
          <p class="slot-time">${slot.time}</p>
          <h5>${slot.subject} · ${slot.topic}</h5>
          <p>${slot.grade}</p>
          <p><strong>Status:</strong> ${isFilled ? "Volunteer assigned" : "Open for volunteer"}</p>
        `;
        slotItems.appendChild(slotCard);

        if (!isFilled) {
          const option = document.createElement("option");
          option.value = slot.slot_id;
          option.textContent = `${day} | ${slot.time} | ${slot.grade} | ${slot.subject}`;
          slotSelect.appendChild(option);
        }
      });

      dayCard.appendChild(slotItems);
      scheduleList.appendChild(dayCard);
    });
  }

  function renderHandbook(data) {
    const { slot, handbook } = data;
    handbookDiv.innerHTML = `
      <h4>Lesson Handbook</h4>
      <p><strong>Assigned slot:</strong> ${slot.day}, ${slot.time}</p>
      <p><strong>Class:</strong> ${slot.grade} · ${slot.subject}</p>
      <p><strong>Topic:</strong> ${slot.topic}</p>
      <div class="handbook-section">
        <h5>45-minute course structure</h5>
        <ul>${handbook.course_structure.map((item) => `<li>${item}</li>`).join("")}</ul>
      </div>
      <div class="handbook-section">
        <h5>Homework to assign</h5>
        <ul>${handbook.homework.map((item) => `<li>${item}</li>`).join("")}</ul>
      </div>
      <div class="handbook-section">
        <h5>Last 5 minutes: life skill emphasis</h5>
        <p>${handbook.life_skill_focus}</p>
      </div>
    `;
    handbookDiv.classList.remove("hidden");
  }

  async function loadPage() {
    try {
      const [resourcesResponse, scheduleResponse] = await Promise.all([
        fetch("/api/resources"),
        fetch("/api/schedule"),
      ]);

      const [resources, schedule] = await Promise.all([
        resourcesResponse.json(),
        scheduleResponse.json(),
      ]);

      renderTeacherResources(resources);
      renderSchedule(schedule);
    } catch (error) {
      resourcesList.innerHTML = "<p>Failed to load teacher resources.</p>";
      scheduleList.innerHTML = "<p>Failed to load schedule.</p>";
      console.error("Error loading app data:", error);
    }
  }

  signupForm.addEventListener("submit", async (event) => {
    event.preventDefault();

    const name = document.getElementById("name").value.trim();
    const email = document.getElementById("email").value.trim();
    const slotId = slotSelect.value;

    handbookDiv.classList.add("hidden");

    try {
      const response = await fetch(
        `/api/schedule/${encodeURIComponent(slotId)}/signup?email=${encodeURIComponent(email)}&name=${encodeURIComponent(name)}`,
        { method: "POST" }
      );

      const result = await response.json();

      if (!response.ok) {
        showMessage(result.detail || "An error occurred", "error");
        return;
      }

      showMessage(result.message, "success");
      renderHandbook(result);
      signupForm.reset();
      await loadPage();
    } catch (error) {
      showMessage("Failed to sign up for the class. Please try again.", "error");
      console.error("Error signing up for slot:", error);
    }
  });

  loadPage();
});
