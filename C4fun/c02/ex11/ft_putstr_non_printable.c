/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putstr_non_printable.c                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hakarata <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/08/01 15:03:42 by hakarata          #+#    #+#             */
/*   Updated: 2022/08/03 08:32:01 by hakarata         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include<unistd.h>

void	ft_putchar(char c)
{
	write(1, &c, 1);
}

int	printable_controller(char c)
{
	if (c >= 32 && c <= 126)
		return (1);
	else
		return (0);
}

void	ft_putstr_non_printable(char *str)
{
	int	i;

	i = 0;
	while (str[i] != '\0')
	{
		if (printable_controller(str[i]) == 1)
			ft_putchar(str[i]);
		else
		{
			ft_putchar('\\');
			ft_putchar("0123456789abcdef"[str[i] / 16]);
			ft_putchar("0123456789abcdef"[str[i] % 16]);
		}
		i++;
	}
}
