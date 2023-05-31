import React, { useState, useEffect } from 'react';
import axios from 'axios';

const DashboardButton = () => {
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [modalData, setModalData] = useState({});

  useEffect(() => {
    if (isModalOpen) {
      fetchData();
    }
  }, [isModalOpen]);

  const fetchData = async () => {
    try {
      const response = await axios.get('http://localhost:5000/dashboard');
      console.log(response.data.message);
      setModalData(response.data.message);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  const handleButtonClick = () => {
    setIsModalOpen(true);
  };

  const handleCloseModal = () => {
    setIsModalOpen(false);
  };

  const organizeDataByDate = () => {
    const organizedData = {};
    for (const month in modalData) {
      for (const item of modalData[month]) {
        const date = item.date;
        if (organizedData[date]) {
          const existingDate = new Date(organizedData[date].date);
          const currentDate = new Date(item.date);
          if (currentDate > existingDate) {
            organizedData[date] = item;
          }
        } else {
          organizedData[date] = item;
        }
      }
    }
    return organizedData;
  };

  const calendarData = organizeDataByDate();

  const getMonthName = (dateString) => {
    const date = new Date(dateString);
    const options = { month: 'long' };
    return new Intl.DateTimeFormat('en-US', options).format(date);
  };

  const getMoodColorClass = (mood) => {
    switch (mood) {
      case 'Negative':
        return 'mood-negative';
      case 'Positive':
        return 'mood-positive';
      case 'Neutral':
        return 'mood-neutral';
      default:
        return '';
    }
  };

  const renderCalendar = () => {
    const calendarDates = Object.keys(calendarData);

    return calendarDates.map((date) => {
      const item = calendarData[date];
      const monthName = getMonthName(date);
      const moodColorClass = getMoodColorClass(item.mood);

      return (
        <div key={date} className="calendar-day">
          <div className="calendar-month">
            <p>{monthName}</p>
          </div>
          <div className="calendar-date">
            <p>{date.split('-')[2]}</p>
          </div>
          <div className={`calendar-mood ${moodColorClass}`}>
            <p>{item.mood}</p>
          </div>
        </div>
      );
    });
  };

  return (
    <div className="d-flex justify-content-center">
      <button onClick={handleButtonClick} className="btn btn-light">
        Mood Dashboard
      </button>
      {isModalOpen && (
        <div className="modal">
          <div className="modal-content">
            <span className="close" onClick={handleCloseModal}>
              &times;
            </span>
            <div className="calendar-container">{renderCalendar()}</div>
          </div>
        </div>
      )}
    </div>
  );
};

export default DashboardButton;
