import React from "react";

export interface IButtonUI extends React.DetailedHTMLProps<React.ButtonHTMLAttributes<HTMLButtonElement>, HTMLButtonElement>{
    children: React.ReactNode,
}