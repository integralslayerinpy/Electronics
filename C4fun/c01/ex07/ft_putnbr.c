/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putnbr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hakarata <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/07/24 12:10:00 by hakarata          #+#    #+#             */
/*   Updated: 2022/07/24 13:51:44 by hakarata         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include<unistd.h>

void	ft_putchar1(char a)
{
	write(1, &a, 1);
}

void	ft_putnbr(int nb)
{
	if (nb == -2147483648)
	{	
		ft_putchar1('-');
		ft_putchar1('2');
		nb = 147483648;
	}
	if (nb < 0)
	{	
		nb = -1 * nb;
		ft_putchar1('-');
	}
	if (nb < 10)
	{	
		ft_putchar1(nb + '0');
	}
	else
	{
		ft_putnbr(nb / 10);
		ft_putnbr(nb % 10);
	}
}
