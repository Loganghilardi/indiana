import React, { useEffect, useState } from 'react';
import Loading from './shared/Loading/Loading';
import { API_URL } from '../config';
import { handleResponse } from '../helpers';

export default function ListMovies() {
  const [loading, setLoading] = useState(false);
  const [movies, setMovies] = useState([]);

  useEffect(() => {
    setLoading(true);
    fetch(`${API_URL}/movies`)
      .then(handleResponse)
      .then((data) => {
        const res_movies = data.content;
        console.log(res_movies);
        setLoading(false);
        setMovies(res_movies);
      });
    // .catch((error) => {
    //   console.log(error.errorMessage);
    //   setLoading(false);
    // });
  });

  if (loading && movies == []) {
    return (
      <div className="loading-container">
        <Loading />
      </div>
    );
  }

  return (
    <div className="table-container">
      <div className="h2 text-center">Liste Movies</div>
      <br />
      <br />
      <table className="table table-striped">
        <thead className="Table-head">
          <tr>
            <th>Titre</th>
            <th>Titre Original</th>
            <th>Année</th>
            <th>Genre</th>
            <th>Rating</th>
          </tr>
        </thead>
        <tbody>
          {movies.map((movie) => (
            <tr key={movie.title}>
              <td>
                <span>{movie.title}</span>
              </td>
              <td>
                <span>{movie.titleOrigine}</span>
              </td>
              <td>
                <span>{movie.year}</span>
              </td>
              <td>
                <span>{movie.genre}</span>
              </td>
              <td>
                <span>{movie.rating}</span>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
