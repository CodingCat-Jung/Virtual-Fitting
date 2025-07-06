import React, { useState } from "react";
import { UserIcon, ShirtIcon, LockIcon } from "lucide-react";
import "./index.css";

function App() {
    const [photo, setPhoto] = useState(null);
    const [clothing, setClothing] = useState(null);

    const handlePhotoUpload = (e) => setPhoto(e.target.files[0]);
    const handleClothingUpload = (e) => setClothing(e.target.files[0]);

    const isReady = photo && clothing;

    return (
        <div className="app-container">
            <header className="app-header">
                <h1 className="title">V-Fitting</h1>
                <a href="/mypage" className="mypage-button">
                    <UserIcon size={28} />
                </a>
            </header>

            <main className="content-container">
                {/* Step 1 */}
                <section className="card">
                    <span className="step-label">Step 1</span>
                    <UserIcon size={48} />
                    <p className="instruction">전신 사진을 업로드 해 주세요.</p>
                    <label className="upload-button">
                        Upload My Photo
                        <input type="file" onChange={handlePhotoUpload} hidden />
                    </label>
                </section>

                {/* Step 2 */}
                <section className="card">
                    <span className="step-label">Step 2</span>
                    <ShirtIcon size={48} />
                    <p className="instruction">입어볼 옷 사진을 업로드 해 주세요.</p>
                    <label className="upload-button">
                        Upload Clothing
                        <input type="file" onChange={handleClothingUpload} hidden />
                    </label>
                </section>

                {/* Try On 버튼 */}
                <button
                    className={`tryon-button ${isReady ? "" : "disabled"}`}
                    disabled={!isReady}
                >
                    <LockIcon size={16} style={{ marginRight: "8px" }} />
                    Try On
                </button>
            </main>
        </div>
    );
}

export default App;
