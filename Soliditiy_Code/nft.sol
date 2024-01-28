// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract MyNFT is ERC721, Ownable {
    // Counter to keep track of token IDs
    uint256 private _tokenIdCounter;

    // Base URI for metadata
    string private _baseTokenURI;

    // Event emitted when a new NFT is minted
    event Minted(address indexed owner, uint256 tokenId);

    constructor(string memory name, string memory symbol, string memory baseTokenURI)
        ERC721(name, symbol)
        Ownable(msg.sender)  // Pass msg.sender as the initialOwner
    {
        _baseTokenURI = baseTokenURI;
    }

    // Function to mint a new NFT
    function mint(address to) external onlyOwner {
        uint256 tokenId = _tokenIdCounter;
        _safeMint(to, tokenId);
        _tokenIdCounter += 1;

        emit Minted(to, tokenId);
    }

    // Function to set the base URI for metadata
    function setBaseURI(string memory baseTokenURI) external onlyOwner {
        _baseTokenURI = baseTokenURI;
    }

    // Function to get the base URI for metadata
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }
}
