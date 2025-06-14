from __future__ import annotations

import pytorch_lightning as pl
from torch import nn
from torch.utils.data import DataLoader, TensorDataset
import torch


def train_model(data: torch.Tensor, labels: torch.Tensor, epochs: int = 1) -> nn.Module:
    dataset = TensorDataset(data, labels)
    loader = DataLoader(dataset, batch_size=32)

    class SimpleModel(pl.LightningModule):
        def __init__(self):
            super().__init__()
            self.l1 = nn.Linear(data.size(1), 1)

        def forward(self, x):
            return self.l1(x)

        def training_step(self, batch, batch_idx):
            x, y = batch
            y_hat = self(x).squeeze()
            loss = nn.functional.mse_loss(y_hat, y)
            self.log("train_loss", loss)
            return loss

        def configure_optimizers(self):
            return torch.optim.Adam(self.parameters(), lr=1e-3)

    model = SimpleModel()
    trainer = pl.Trainer(max_epochs=epochs, logger=False, enable_checkpointing=False)
    trainer.fit(model, loader)
    return model
