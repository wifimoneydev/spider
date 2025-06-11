# t2cvision

This is an AI project I’m building to help solve a very real problem in developing countries — waste management and recycling. The idea is simple: use computer vision to identify different types of trash (plastic, nylon, cans, etc.) so that people can automatically exchange waste for cash at smart outlets.

The bigger picture here is a recycling system powered by AI — one where people drop their waste into a machine, and it detects, sorts, and rewards them instantly. That’s what I’m working toward with Trash2Cash (T2C), and `t2cvision` is the brain that will power it.

## What I’ve Done So Far

* ✅ Set up the folder structure and environment using TensorFlow/Keras.
* ✅ Collected and organized the [TrashNet dataset](https://github.com/garythung/trashnet).
* ✅ Built and trained a basic CNN model to classify trash images.
* ✅ Created preprocessing scripts for image resizing and augmentation.

## Where It’s At Now

The model runs and trains, but honestly — the accuracy isn’t there yet. It’s struggling to correctly identify trash categories consistently, especially between materials like nylon vs. plastic. I’ve tried adjusting the architecture and tuning the hyperparameters, but the performance still isn’t reliable.

## Next Steps

Right now, I’m exploring the idea of **building my own custom dataset** — one that’s more relevant to local trash types in Nigeria (pure water sachets, PET bottles, local-style packaging, etc.). I think that will give me better results than trying to rely on datasets made for other environments.

The long-term plan is to integrate this into a real-world, AI-powered trash-to-cash outlet that runs smoothly with automation.

---

## Why This Matters

I’m passionate about using AI to solve problems that actually matter — not just building models for leaderboard scores. If this works, it can give people a real incentive to clean up their environment and earn a bit of income, while also improving recycling systems from the ground up.

---

## Tech Stack

* Python
* TensorFlow / Keras
* NumPy / Pandas
* Matplotlib (for training viz)
* TrashNet dataset (custom dataset coming soon)

---

Still a work in progress, but I’m fully in. Stay tuned. 👀
