/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_atoi.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hakarata <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/08/06 09:36:31 by hakarata          #+#    #+#             */
/*   Updated: 2022/08/06 11:13:52 by hakarata         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include<unistd.h>

int	ft_atoi(char *str)
{
	int	i;
	int	cast;
	int	total;

	i = 0;
	cast = 1;
	total = 0;
	while ((str[i] >= '\t' && str[i] <= '\r') || str[i] == ' ')
		i++;
	while (str[i] == '+' || str[i] == '-')
	{
		if (str[i] == '-')
			cast = cast * -1;
		i++;
	}
	while (str[i] >= '0' && str[i] <= '9')
	{
		total = (str[i] - '0') + (total * 10);
		i++;
	}
	return (total * cast);
}
