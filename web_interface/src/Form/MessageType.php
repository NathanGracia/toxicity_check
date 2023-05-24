<?php

namespace App\Form;

use App\Entity\Message;
use Symfony\Component\Form\AbstractType;
use Symfony\Component\Form\Extension\Core\Type\RangeType;
use Symfony\Component\Form\FormBuilderInterface;
use Symfony\Component\OptionsResolver\OptionsResolver;

class MessageType extends AbstractType
{
    public function buildForm(FormBuilderInterface $builder, array $options): void
    {

        $toxicityValue = $options['data']->getToxicity() ?? 0;

        $builder
            ->add('content')
            ->add('toxicity', RangeType::class, [
                'attr' => [
                    'min' => 0,
                    'max' => 1,
                    'step' => 0.01,
                    'class' => 'form-range',
                    'id' => 'toxicitySlider',
                ],
                'data' => $toxicityValue,
            ]);
    }

    public function configureOptions(OptionsResolver $resolver): void
    {
        $resolver->setDefaults([
            'data_class' => Message::class,
        ]);
    }
}
