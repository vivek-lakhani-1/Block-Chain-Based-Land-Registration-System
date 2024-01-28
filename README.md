# Land Registration System using Blockchain and NFT Minting

## Overview
The Land Registration System is a decentralized application (DApp) built on blockchain technology with integrated NFT minting capabilities. It aims to provide a secure, transparent, and immutable platform for registering land parcels and converting them into Non-Fungible Tokens (NFTs). These NFTs represent unique digital assets with verifiable ownership records, ensuring trust and efficiency in land transactions. The system incorporates features such as Metamask integration for secure signing, precise land registration using longitude and latitude coordinates, different administrative levels for governance, and displaying amenities around registered land parcels.

## Features

### 1. Metamask Integration
   - **Description**: Metamask is integrated into the system to facilitate secure transaction signing, ensuring user privacy and authenticity.
   - **Usage**: Users can connect their Metamask wallets to the DApp and securely sign transactions related to land registration and NFT generation.

### 2. Land Registration
   - **Description**: Users can register land parcels on the platform using longitude and latitude coordinates, ensuring precise location data.
   - **Usage**: Users provide detailed information about the land parcel, including its boundaries, ownership details, and relevant documents.

### 3. Administrator Levels
   - **Description**: The system includes different administrative levels to manage land registration and governance.
   - **Land Inspector**: Responsible for verifying land details, conducting inspections, and ensuring the authenticity of registered land parcels.
   - **Super Admin Government**: Holds governance rights and oversees the overall functioning of the system, including user management and policy enforcement.

### 4. NFT Minting
   - **Description**: Registered land parcels are converted into unique NFTs (ERC-721 tokens), providing immutable ownership records and facilitating transparent land transactions.
   - **Usage**: Upon successful land registration, the system automatically generates a corresponding NFT representing the registered land parcel.

### 5. Amenities Display
   - **Description**: Users can view amenities and infrastructure around registered land parcels, aiding in decision-making processes for potential buyers or lessees.
   - **Usage**: The system utilizes geolocation data to display nearby amenities such as schools, hospitals, transportation hubs, and recreational facilities.

## Installation
To install and run the Land Registration System on your local machine, follow these steps:

1. **Clone the repository**: 
   ```
   git clone https://github.com/your/repository.git
   ```

2. **Install dependencies**:
   ```
   cd project-folder
   npm install
   ```

3. **Configure environment variables**:
   ```
   Create a .env file and add necessary variables such as API keys, Ethereum wallet addresses, etc.
   ```

4. **Run the application**:
   ```
   npm start
   ```

## Usage
1. **User Registration**: Users can sign up on the platform using Metamask and provide necessary details for account creation.
2. **Land Registration**: Users with appropriate permissions (e.g., Land Inspector) can register land parcels using longitude and latitude coordinates.
3. **NFT Generation**: Upon successful registration, the system automatically converts the land parcel into a unique NFT.
4. **Amenities Display**: Users can explore amenities around the registered land, aiding in decision-making processes.
5. **Transaction**: Users can engage in transparent land transactions using the generated NFTs, ensuring immutable ownership records.

