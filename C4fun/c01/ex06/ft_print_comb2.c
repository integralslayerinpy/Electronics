/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_comb2.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hakarata <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/07/24 09:48:59 by hakarata          #+#    #+#             */
/*   Updated: 2022/07/24 11:34:45 by hakarata         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include<unistd.h>

void	ft_putchar1(char a)
{
	write(1, &a, 1);
}

void	ft_print_comb2(void)
{
	int		i;
	int		j;		

	i = -1;
	while (i++ < 98)
	{
		j = i;
		while (j++ < 99)
		{
			ft_putchar1((i / 10) + '0');
			ft_putchar1((i % 10) + '0');
			ft_putchar1(' ');
			ft_putchar1((j / 10) + '0');
			ft_putchar1((j % 10) + '0');
			if (i != 98)
			{		
				ft_putchar1(',');
				ft_putchar1(' ');
			}
		}	
	}
}
